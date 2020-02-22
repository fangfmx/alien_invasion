#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ship.py
#  
#  Copyright 2020 lizy <674051537@qq.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pygame

class Ship():
	def __init__(self,screen):
		"""初始化飞船并设置初始位置"""
		self.screen=screen
		
		# 加载飞船图像并获取其外接矩形
		self.image=pygame.image.load("images/ship.bmp")
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		# 将每艘飞船放在屏幕底部中央
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
	def blitme(self):
		"""在指定位置绘制飞船"""	
		self.screen.blit(self.image,self.rect)
		
		
		
		
		
		



