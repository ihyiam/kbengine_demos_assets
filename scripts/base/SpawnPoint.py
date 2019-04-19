# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObject import GameObject
import EntityDef as Def
import Types

@Def.entity()
class SpawnPoint(KBEngine.Entity, GameObject):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)
		self.createCellEntity(self.createToCell)
		
	@Def.property(flags=Def.BASE, persistent=True)
	def createToCell(self) -> Def.ENTITYCALL:
		return None

