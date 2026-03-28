# -*- coding: utf-8 -*-
"""Base widget class with SVG rendering capabilities.

This module provides the foundation for all LCARS widgets, including SVG rendering,
styling, and interactive feedback functionality. It handles dynamic SVG generation,
caching of rendered images, and font management for consistent UI styling.
"""
from typing import Optional
from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
import os
import xxhash
import os.path


class Widgets:
    """Base class for LCARS widgets with SVG rendering support.

    Provides common functionality for all LCARS widgets including SVG rendering,
    stylesheet management, font handling, and visual feedback effects. Implements
    SVG caching to improve performance and supports dynamic color substitution.

    Attributes:
        default_style: Base stylesheet template for widgets.
        svg: SVG template string with placeholders for dynamic values.
        toggle: Toggle state for visual feedback effects.
        lcars: Reference to the parent LCARS window.
        default_font: Default font for widget text.
        default_font_name: Name of the default font (typically "LCARS").
        image_folder: Directory for caching rendered SVG images.
        background_col: Default background color.
        style: Current stylesheet.
        color: Current widget color.
        rect: Geometry rectangle of the widget.
    """
    default_style: str = "border: none;\nbackground: {bg};\nText-align: right;"
    svg: Optional[str]
    toggle: bool
    lcars: QtWidgets.QWidget
    default_font: QtGui.QFont
    default_font_name: str
    image_folder: str
    background_col: str
    style: str
    color: str
    rect: QtCore.QRect

    def __init__(self, lcars: QtWidgets.QWidget, svg: Optional[str] = None) -> None:
        """Initialize a widget with LCARS styling and SVG support.

        Args:
            lcars: Reference to the parent LCARS window.
            svg: Optional SVG template string for rendering custom shapes.
        """
        self.svg = svg
        self.toggle = False
        self.lcars = lcars
        self.default_font = QtGui.QFont()
        self.default_font_name = "LCARS"
        self.set_default_font()
        self.image_folder = "background"
        self.background_col = "#000"

    def tickle(self, color: str) -> None:
        """Provide visual feedback by temporarily changing widget color.

        Changes the widget color and schedules it to revert after 300ms,
        creating a visual "tickle" or flash effect.

        Args:
            color: The temporary color to display.
        """
        self.paint_back(color)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.tickle_done)
        timer.setSingleShot(True)
        timer.start(300)

    def tickle_done(self) -> None:
        """Revert widget color to original after tickle effect.

        Called after the tickle timer expires to restore the original color.
        """
        self.paint_back(self.color)

    def tockle(self, color: Optional[str] = None) -> None:
        """Toggle between two colors for visual state indication.

        Toggles the widget between a specified color and the default color.
        Can be used to indicate active/inactive or selected/deselected states.

        Args:
            color: The alternate color to toggle to. If None, just toggles
                the state without changing color.
        """
        if not self.toggle and color:
            self.paint_back(color)
        else:
            self.paint_back(self.color)
        self.toggle = not self.toggle

    def set_default_font(self, fontname: Optional[str] = None, size: int = 26) -> None:
        """Set the default font for widgets.

        Args:
            fontname: Font family name (default: "LCARS").
            size: Font size in points (default: 26).
        """
        if not fontname:
            fontname = self.default_font_name
        self.default_font.setFamily(fontname)
        self.default_font.setPointSize(size)
        self.default_font.setStrikeOut(False)

    def adapt_svg(self, color: Optional[str] = None) -> str:
        """Adapt SVG template with widget dimensions and color.

        Substitutes the widget's current dimensions and color into the SVG
        template string to create a customized SVG.

        Args:
            color: Color to use in the SVG. If None, uses the widget's current color.

        Returns:
            The adapted SVG string with substituted values.
        """
        rect: QtCore.QRect = self.rect
        h = rect.height()
        w = rect.width()
        if color is None:
            color = self.color
        #print(self.svg.format(h=h, w=w, c=color))
        #print(self.svg)
        return self.svg.format(h=h, w=w, c=color)

    def build_svg(self, color: Optional[str] = None) -> Optional[str]:
        """Build and cache SVG image for the widget.

        Renders the adapted SVG to a PNG image and caches it. Uses xxhash
        for fast filename generation based on SVG content.

        Args:
            color: Color to use in the SVG. If None, uses the widget's current color.

        Returns:
            Path to the cached PNG image, or None if no SVG is defined.
        """
        if self.svg != "":
            svg = self.adapt_svg(color)
            return self.save_img(svg, QtCore.QSize(self.rect.width(), self.rect.height()))
        return None

    def parse_style(self, style: str, bgcol: Optional[str] = None) -> str:
        """Parse and format stylesheet with background color.

        Args:
            style: Stylesheet template string.
            bgcol: Background color to substitute. If None, uses widget's background color.

        Returns:
            Formatted stylesheet with substituted background color.
        """
        if not bgcol:
            bgcol = self.background_col
        return style.format(bg=bgcol)

    def paint_back(self, color: Optional[str] = None) -> None:
        """Paint the widget background with the specified color.

        If an SVG is defined, renders it and applies as a background image.
        Otherwise, applies a solid color background. Updates the widget's
        stylesheet accordingly.

        Args:
            color: Background color. If None, uses the widget's current color.
        """
        if hasattr(self, 'svg'):
            if self.svg is not None:
                url = self.build_svg(color)
                if hasattr(self, 'paint_pixmap'):
                    self.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), url)))
                style = self.parse_style(self.style, bgcol=self.background_col)
                self.setStyleSheet(style + "\nbackground-image: url(" + url + ");")
                return
        style = self.parse_style(self.style, bgcol=color)
        self.setStyleSheet(style)

    def render_svg(self, svg: str, size: QtCore.QSize) -> QtGui.QImage:
        """Render SVG string to a QImage.

        Uses Qt's SVG renderer to convert an SVG string into a raster image
        with the specified dimensions.

        Args:
            svg: SVG string to render.
            size: Target image dimensions.

        Returns:
            Rendered QImage with ARGB32 format.
        """
        qByteArray = QtCore.QByteArray()
        qByteArray.append(svg)
        renderer = QtSvg.QSvgRenderer(qByteArray)
        qim = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        qim.fill(0)
        painter = QtGui.QPainter()
        painter.begin(qim)
        renderer.render(painter)
        painter.end()
        return qim

    def save_img(self, svg: str, size: QtCore.QSize) -> str:
        """Render and cache SVG as PNG image.

        Renders an SVG to PNG and caches it using a hash-based filename.
        Reuses cached images if the same SVG and size are requested again.
        Uses hierarchical directory structure for cache organization.

        Args:
            svg: SVG string to render.
            size: Target image dimensions.

        Returns:
            Path to the saved PNG image file.
        """
        name = xxhash.xxh64(svg + str(size)).hexdigest()
        path = os.path.join(self.image_folder, name[:3], name[3:6])
        filename = name[6:] + ".png"
        url = os.path.join(path, filename)
        if not os.path.isfile(url):
            if not os.path.isdir(path):
                os.makedirs(path)
            image = self.render_svg(svg, size)
            image.save(url, "PNG")
        return url
