#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alien_invasion.py
#  
#  Copyright 2020 lizy <lizy@SC-201803062125>
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

import sys

import pygame
from settings import Settings
from ship import Ship

def run_game():
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
	pygame.display.set_caption("Alien Invasion")
	
	# ����һ�ҷɴ�
	ship=Ship(screen)
	
	
	# ��ʼ��Ϸ����ѭ��
	while True:
		
		# ÿ��ѭ�������һ����ɫ
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		
		
		# ���Ӽ��̺�����¼�
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		
		# ������Ļ�ɼ�
		pygame.display.flip()

run_game()
