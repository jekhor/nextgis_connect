# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Plugins settings
                                 A QGIS plugin
 Compulink QGIS tools
                             -------------------
        begin                : 2014-10-31
        git sha              : $Format:%H$
        copyright            : (C) 2014 by NextGIS
        email                : info@nextgis.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import
from qgis.PyQt.Qt import Qt
from qgis.PyQt.QtCore import QSize, QPoint
from .ngw_api.qgis.common_plugin_settings import PluginSettings as CommonPluginSettings


class PluginSettings(CommonPluginSettings):

    _company_name = 'NextGIS'
    _product = 'NextGISConnect'

    @classmethod
    def dock_area(cls):
        settings = cls.get_settings()
        return settings.value('/ui/dockWidgetArea', Qt.RightDockWidgetArea, type=int)

    @classmethod
    def set_dock_area(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/dockWidgetArea', val)

    @classmethod
    def dock_floating(cls):
        settings = cls.get_settings()
        return settings.value('/ui/dockIsFloating', False, type=bool)

    @classmethod
    def set_dock_floating(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/dockIsFloating', val)

    @classmethod
    def dock_size(cls):
        settings = cls.get_settings()
        return settings.value('/ui/dockWidgetSize', QSize(150, 300), type=QSize)

    @classmethod
    def set_dock_size(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/dockWidgetSize', val)

    @classmethod
    def dock_pos(cls):
        settings = cls.get_settings()
        return settings.value('/ui/dockWidgetPos', QPoint(500, 500), type=QPoint)

    @classmethod
    def set_dock_pos(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/dockWidgetPos', val)

    @classmethod
    def dock_visibility(cls):
        settings = cls.get_settings()
        return settings.value('/ui/dockWidgetIsVisible', True, type=bool)

    @classmethod
    def set_dock_visibility(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/dockWidgetIsVisible', val)

    @classmethod
    def webgis_creation_message_closed_by_user(cls):
        settings = cls.get_settings()
        return settings.value('/ui/webGisCreationMessageClosedByUser', False, type=bool)

    @classmethod
    def set_webgis_creation_message_closed_by_user(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/webGisCreationMessageClosedByUser', val)

    @classmethod
    def set_auto_open_web_map_option(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/autoOpenWebMapByDefault', val)

    @classmethod
    def auto_open_web_map_option(cls):
        settings = cls.get_settings()
        return settings.value('/ui/autoOpenWebMapByDefault', True, type=bool)

    @classmethod
    def set_auto_add_wfs_option(cls, val):
        settings = cls.get_settings()
        settings.setValue('/ui/autoAddWFSByDefault', val)

    @classmethod
    def auto_add_wfs_option(cls):
        settings = cls.get_settings()
        return settings.value('/ui/autoAddWFSByDefault', True, type=bool)
