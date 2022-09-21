from decimal import *
getcontext().prec = 9
def calculate():
	from decimal import Decimal
	getcontext().prec = 9
	print("What Are You Looking For?")
	print("A. RP at certain amount of GEs")
	print("B. BEs received from a specific boss level")
	print("C. Total BEs at a certain level")
	print("D. Amount of GEs from BEs")
	print("E. Water egg reduction")
	print("F. Cost to level up misc. 13 easter egg by 1")
	print("G. Cumalative cost of misc 13 easter eggs")
	print("H. Levels to buy for each easter egg with a specified amount of BEs")
	print("I. Cost to level up main 7 easter egg by 1")
	print("J. Cumalative cost of main 7 easter eggs")
	print("K. How many phoenix egg levels to buy with a specified amount of GEs")
	print("L. Chicken Health at Specific Levels")
	
	print("************************************************************************")
	
	UC= input("Please type the letter of the option that matches what you need:")
	if UC.upper() == "A":
		Total_GE = input("Total GE earned:")
		TG= float(Total_GE)
		A= float(-0.0003 * TG)
		B= float(2.7182818284590452353602874713527 ** A)
		C= float(B * 23)
		D= float(25-C)
		E= float(D *.01)
		F= Decimal(E)
		TRP= float(F * 100)
		TRPS= str(TRP)
		Toe= str(E)
		print("Multiplier:" + Toe)
		print("Rebirth Power" + TRPS + "%")
		print("************************************************************************")
	
	if UC.upper() == "B":
		Total_GE = input("Total GE earned:")
		TG= float(Total_GE)
		A= float(-0.0003 * TG)
		B= float(2.7182818284590452353602874713527**A)
		C= float(B*23)
		D= float(25-C)
		E= float(D*.01)
		F= Decimal(E)
		TRP= float(E * 100)
		TRPS= str(TRP)
		Toe= str(E)
		print("Multiplier:" + Toe)
		print("Rebirth Power:" + TRPS + "%")
		EarthEggLevel = input("Earth Egg Level:")
		Level= input("Farm Level:")
		Farm_LevelDeci= Decimal(Level)
		EE_LevelFloat= float(EarthEggLevel)
		BEBossAEqua1= float(10*EE_LevelFloat**2+1)
		BEBossAEqua1Deci= Decimal(BEBossAEqua1)
		#Jen= float(10*Josh**2)
		BEBossAEqua2= float(Farm_LevelDeci - 80)/25
		BEBossAEqua3= float(BEBossAEqua2)**1.3
		BEBossAEqua3Deci= Decimal(BEBossAEqua3)
		BEBossAEqua4= float(Farm_LevelDeci/5)-20
		BEBossAEqua4Deci= Decimal(BEBossAEqua4)
		BEBossAEqua5= (20*(1+F)**BEBossAEqua4Deci)
		BEBossAEqua5Deci= Decimal(BEBossAEqua5)
		BEBossAEquaAdd= (BEBossAEqua5Deci + BEBossAEqua3Deci)
		BEBossAEquaAddDeci= Decimal(BEBossAEquaAdd)
		BEBossAEquaFin= Decimal(BEBossAEquaAddDeci*BEBossAEqua1Deci)
		BEBossAEquaFinStr= str(BEBossAEquaFin)
		print("Black Eggs at Specified Level:" + BEBossAEquaFinStr)
		print("************************************************************************")
	
	if UC.upper() == "C":
		import decimal
		from decimal import Decimal
		Farm_lvlTot= input("Farm Level:")
		Farm_lvlTotDeci= Decimal(Farm_lvlTot)
		Farm_lvlTotDeci2= Decimal(Farm_lvlTotDeci / 5)	
		Farm_lvlTotDeci3= int(Farm_lvlTotDeci2)	
		Farm_lvlTotRange= range(16, Farm_lvlTotDeci3)
		def sigma(Farm_lvlTotRange):
			import math
			from math import e
			import decimal
			from decimal import Decimal
			EE_CIn = int(input("Earth Egg Level:"))
			EE_CInDeci = Decimal(10 * (EE_CIn ** 2) + 1)
			#print(EE_CInDeci)
			GE_CIn = int(input("Number of GEs:"))
			GE_CInDeci = Decimal(GE_CIn)
			GE_CEquaCon1 = Decimal(-0.0003)
			GE_CEqua1 = Decimal(25 - 23 * (Decimal(math.e)) ** (GE_CEquaCon1 * GE_CInDeci))
			GE_CEqua2 = Decimal(GE_CEqua1 / 100)
			GE_CEqua2Deci = Decimal(GE_CEqua2)
			F_LvlCCon1 = Decimal(1.3)
			F_LvlC = Decimal(((Farm_lvlTotDeci - 80) / 25) ** F_LvlCCon1)
			F_LvlCDeci = Decimal(F_LvlC)
			Best= []
			for i in (Farm_lvlTotRange):
				GE_CEqua3 = Decimal(EE_CInDeci * (20 * (1 + GE_CEqua2Deci) ** (i - 20) + F_LvlCDeci))
				#print(GE_CEqua3)
				Best.append(GE_CEqua3)
				My_SetSum = sum(Best)
				My_SetSumDeci = Decimal(My_SetSum)
			print("Estimated Amount of Total BEs by Specified Level:", My_SetSumDeci)
		sigma(Farm_lvlTotRange)
			
	print("************************************************************************")
	
	import math
	from decimal import MAX_EMAX
	from decimal import Decimal
	if UC.upper() == "D":
		TotalBEEarnedIn= input("Total BE Earned:")
		TotalBEEarnedInDeci= Decimal(TotalBEEarnedIn)
		TotalBEEarnedInInt= int(TotalBEEarnedInDeci)
		TotalBEEarnedEquaFin= Decimal(math.log10(TotalBEEarnedInInt ** 5))
		TotalBEEarnedEquaFinDeci= Decimal(TotalBEEarnedEquaFin)
		TotalBEEarnedEquaFinDeci2= Decimal(TotalBEEarnedEquaFinDeci)
		TotalBEEarnedEquaFinDeci2Str= str(TotalBEEarnedEquaFinDeci2)
		print("Total GE Earned:" + TotalBEEarnedEquaFinDeci2Str)
		print("************************************************************************")
	
	if UC.upper() == "E":
		WE_LevelIn= input("Water egg level:")
		WE_LevelInFl= float(WE_LevelIn)
		WE_Equa= Decimal(100*(1-0.95**WE_LevelInFl))
		WE_EquaDiv= Decimal(WE_Equa/100)
		WE_EquaDivDeci= Decimal(WE_EquaDiv)
		WE_EquaDivDeciStr= str(WE_EquaDivDeci)
		if WE_LevelInFl <= 0:
	 	 Cena= 1
		WE_ReducP=float(WE_EquaDivDeci * -100)
		WE_ReducPSstr= str(WE_ReducP)
		print("Water egg reduction:" + WE_EquaDivDeciStr)
		print("Water egg reduction % form:" + WE_ReducPSstr + "%")
		print("************************************************************************")
	
	#Level up cost of Miscellaneous 13 Easter eggs↓↓↓
	if UC.upper() == "F":
		WE_LevelIn= input("Water egg level:")
		WE_LevelInFl= float(WE_LevelIn)
		WE_Equa= Decimal(100*(1-0.95**WE_LevelInFl))
		WE_EquaDiv= Decimal(WE_Equa/100)
		WE_EquaDivDeci= Decimal(WE_EquaDiv)
		WE_EquaDivDeciStr= str(WE_EquaDivDeci)
		if WE_LevelInFl <= 0:
	 	 Cena= 1
		WE_ReducP=float(WE_EquaDivDeci * -100)
		WE_ReducPSstr= str(WE_ReducP)
		print("Water egg reduction:" + WE_EquaDivDeciStr)
		print("Water egg reduction % form:" + WE_ReducPSstr + "%")
		M13_EECurr= input("Current Level Of 13 Miscellaneous Eggs:")
		M13_EECurrDeci= Decimal(M13_EECurr)
		M13EE_CostEqua= Decimal(2**(M13_EECurrDeci + 1)* WE_EquaDivDeci)
		M13EE_CostEquaStr= str(M13EE_CostEqua)
		print("Level Up Cost Of 13 Miscellaneous Eggs:" + M13EE_CostEquaStr)
		print("************************************************************************")
	
	#Easter Egg miscellaneous 13 cumulative cost calculations↓↓↓
	if UC.upper() == "G":
		WE_LevelIn= input("Water egg level:")
		WE_LevelInFl= float(WE_LevelIn)
		WE_Equa= Decimal(100*(1-0.95**WE_LevelInFl))
		WE_EquaDiv= Decimal(WE_Equa/100)
		WE_EquaDivDeci= Decimal(WE_EquaDiv)
		WE_EquaDivDeciStr= str(WE_EquaDivDeci)
		if WE_LevelInFl <= 0:
	 	 Cena= 1
		WE_ReducP=float(WE_EquaDivDeci * -100)
		WE_ReducPSstr= str(WE_ReducP)
		print("Water egg reduction:" + WE_EquaDivDeciStr)
		print("Water egg reduction % form:" + WE_ReducPSstr + "%")
		M13_EELvlWant= input("13 Miscellaneous Easter egg levels Wanted:")
		M13_EELvlWantedDeci= Decimal(M13_EELvlWant)
		M13_EELvlCumCost= Decimal(2 **(M13_EELvlWantedDeci + 1) - 3)
		WE_EffInv= Decimal(1 - WE_EquaDivDeci)
		M13_EELvlCumCostFin= Decimal(M13_EELvlCumCost * WE_EffInv)
		M13_EELvlCumCostAllFin= Decimal(M13_EELvlCumCostFin * 13)
		M13_EELvlCumCostAllFinStr= str(M13_EELvlCumCostAllFin)
		M13_EELvlCumCostFinDeci= Decimal(M13_EELvlCumCostFin)
		M13_EELvlCumCostFinDeciStr= str(M13_EELvlCumCostFinDeci)
		print("Cumulative Cost Of One Misc 13 Easter Egg At Specified Level:" + M13_EELvlCumCostFinDeciStr)
		print("Cumulative Cost of All Misc 13 Easter Eggs At Specified Level:" + M13_EELvlCumCostAllFinStr)
		print("************************************************************************")
	
	#Levels to buy for ALL easter eggs calculations↓↓↓
	if UC.upper() == "H":
		import math
		Black_EggsTot= input("Amount Of BEs Retiring With:")
		WaterEggIn= input("Water Egg Level:")
		WaterEggInDec= Decimal(WaterEggIn)
		BE13ROC= Decimal(0.95)
		WaterEggRate= Decimal(1 - (BE13ROC ** 					WaterEggInDec))
		WaterEggRateInv= Decimal(1 - WaterEggRate)
		Black_EggsNum= Decimal(Black_EggsTot)
		BE_13Divisor= Decimal(.10)
		BE_13P= Decimal(Black_EggsNum * 							BE_13Divisor)
		BE_13PT= Decimal(BE_13P / WaterEggRateInv)
		BE_13Single= int(BE_13PT / 13)
		BE_13SingleCont1= int(1)
		BE_13SingleCont2= Decimal(1.0000000000000)
		BE_13EggsToBuy= Decimal(math.log2(BE_13Single + BE_13SingleCont1))
		BE_13EggsToBuyT= Decimal(BE_13EggsToBuy)
		BE_13EggsToBuy2= Decimal(BE_13EggsToBuyT - BE_13SingleCont2)
		BE_13EggsToBuyDeci= Decimal(BE_13EggsToBuy2)
		BE_13EggsToBuyStr= str(BE_13EggsToBuyDeci)
		print("Upgrade Misc 13 Easter Egg Levels To:" + 	BE_13EggsToBuyStr)
		BE_7Divisor= Decimal(.45)
		BE_7P= Decimal(Black_EggsNum * BE_7Divisor)
		BE_7PT= Decimal(BE_7P / WaterEggRateInv)
		BE_7Single= Decimal(BE_7PT / 7)
		BE_7Cont1= Decimal(0.25)
		BE_7Cont2= Decimal(0.50)
		BE_7EquUncomp= Decimal((BE_7Single * 2) + 		BE_7Cont1)
		BE_7EquSq= Decimal(BE_7EquUncomp.sqrt())
		BE_7EggsToBuy= Decimal(BE_7EquSq - 					BE_7Cont2)
		BE_7EggsToBuyStr= str(BE_7EggsToBuy)
		print("Upgrade Main 7 Easter Egg Levels To:" + 		BE_7EggsToBuyStr)
		Turtle_EggCont1= Decimal(0.20)
		Turtle_EggCont2= Decimal(0.40)
		TurtleWaterMulti= Decimal(1 + WaterEggRateInv)
		Turtle_EggEqua= Decimal(((Black_EggsNum * 		Turtle_EggCont1) * TurtleWaterMulti) ** 					Turtle_EggCont2)
		Turtle_EggEquaStr= str(Turtle_EggEqua)
		print("Upgrade Turtle Egg Level To:" + 						Turtle_EggEquaStr)
		GK_EggCont1= Decimal(0.20)
		GK_EggEqua= Decimal(Black_EggsNum * 				GK_EggCont1)
		GK_EggEquaStr= str(GK_EggEqua)
		print("Upgrade GoodKnight Egg Level To:" + 			GK_EggEquaStr)
		print("************************************************************************")
	#Level up cost of main 7 easter eggs↓↓↓
	if UC.upper() == "I":
		WE_LevelIn= input("Water egg level:")
		WE_LevelInFl= float(WE_LevelIn)
		WE_Equa= Decimal(100*(1-0.95**WE_LevelInFl))
		WE_EquaDiv= Decimal(WE_Equa/100)
		WE_EquaDivDeci= Decimal(WE_EquaDiv)
		WE_EquaDivDeciStr= str(WE_EquaDivDeci)
		if WE_LevelInFl <= 0:
	 	 Cena= 1
		WE_ReducP=float(WE_EquaDivDeci * -100)
		WE_ReducPSstr= str(WE_ReducP)
		WE_EffInv= Decimal(1 - WE_EquaDivDeci)
		WE_EffInvDeci= Decimal(WE_EffInv)
		print("Water egg reduction:" + WE_EquaDivDeciStr)
		print("Water egg reduction % form:" + WE_ReducPSstr + "%")
		M7_EELvlWant= input("Current Level Of Main 7 Eggs:")
		M7_EELvlWantDeci= Decimal(M7_EELvlWant)
		M7_EELvlCost1= Decimal(M7_EELvlWantDeci + 1) * WE_EffInvDeci
		M7_EELvlCost1Str= str(M7_EELvlCost1)
		print("Level Up Cost Of Main 7 Egg By One:" + M7_EELvlCost1Str)
		
		print("************************************************************************")
	
	#Easter Egg Main 7 Cost Calculations↓↓↓
	if UC.upper() == "J":
		WE_LevelIn= input("Water egg level:")
		WE_LevelInFl= float(WE_LevelIn)
		WE_Equa= Decimal(100*(1-0.95**WE_LevelInFl))
		WE_EquaDiv= Decimal(WE_Equa/100)
		WE_EquaDivDeci= Decimal(WE_EquaDiv)
		WE_EquaDivDeciStr= str(WE_EquaDivDeci)
		if WE_LevelInFl <= 0:
	 	 Cena= 1
		WE_ReducP=float(WE_EquaDivDeci * -100)
		WE_ReducPSstr= str(WE_ReducP)
		WE_EffInv= Decimal(1 - WE_EquaDivDeci)
		WE_EffInvDeci= Decimal(WE_EffInv)
		print("Water egg reduction:" + WE_EquaDivDeciStr)
		print("Water egg reduction % form:" + WE_ReducPSstr + "%")
		M7_EEIn= input("Main 7 Easter Egg Levels Wanted:")
		M7_EEInDeci= Decimal(M7_EEIn)
		M7_EEEqua1= Decimal(M7_EEInDeci+1)
		M7_EEEqua2 = Decimal(M7_EEEqua1*M7_EEInDeci)
		M7_EEEquaCon1= Decimal(0.5)
		M7_EEEqua3= Decimal(M7_EEEqua2 * M7_EEEquaCon1)
		M7_EEEqua3Deci= Decimal(M7_EEEqua3
		)
		M7_EEEquaInvIn= Decimal(M7_EEEqua3Deci * WE_EffInvDeci)
		M7_EEEqua4= Decimal(M7_EEEquaInvIn)
		M7_EEEqua4Str= str(M7_EEEqua4)
		M7_EEEqua5Sing= Decimal(M7_EEEqua4 / 7)
		M7_EEEqua5SingDeci= Decimal(M7_EEEqua5Sing)
		M7_EEEqua5SingDeciStr= str(M7_EEEqua5SingDeci)
		print("Cumulative Cost of Main 7 Easter Eggs At Specified Level:" + M7_EEEqua4Str)
		print("Cumulative Cost Of 1 Main 7 Easter Egg:" + M7_EEEqua5SingDeciStr)
		print("************************************************************************")
	
	
	
	
	
	if UC.upper() == "K":
		GoldenEggs= float(input("Life Time GEs:"))
		a= 799
		c= 1300
		b= 1
		d= 1500
		e= 1501
		f= 1444
		if GoldenEggs < c:
			Earth= int(GoldenEggs * .39)
			if Earth < b:
				Earth= 0
		if GoldenEggs >= c:
			Earth = int(528)
		import math
		ELC= int(math.sqrt((2 * Earth) + 0.25) - 0.5)
		EECC= int((ELC * (ELC + 1)) / 2)
		if GoldenEggs < a:
			Water= int(GoldenEggs * .12)
		if GoldenEggs >= a:
			Water= int(GoldenEggs * 0.19)
			if Water < b:
				Water = 0
		if GoldenEggs >= f:
			Water= 406
		WLC= int(math.sqrt((2 * Water) + 0.25) - 0.50)
		WECC= int((WLC * (WLC + 1)) / 2)
		if GoldenEggs < a:
			Fire= int(GoldenEggs * .10)
		if GoldenEggs >= a:
			Fire= int(GoldenEggs*.06)
		if GoldenEggs >=e:
			Fire= int(GoldenEggs*.01)
			if Fire < b:
				Fire = 0
		if GoldenEggs < a:
			Magnetism= int(GoldenEggs * .06)
		if GoldenEggs >= a:
			Magnetism= int(GoldenEggs * .08)
		if GoldenEggs >= e:
			Magnetism= int(GoldenEggs * .10)
			if Magnetism < b:
				Magnetism = 0
		MLC= int(math.sqrt((2 * Magnetism) + 0.25) - 0.5)
		MECC= int((MLC * (MLC + 1)) / 2)
		if GoldenEggs < a:
			Wind= int(GoldenEggs * .03)
		if GoldenEggs >= a:
			Wind= int(GoldenEggs * .04)
		if GoldenEggs >=e:
			Wind= int(GoldenEggs * .04)
			if Wind < b:
				Wind = 0
		WiLC= int(math.sqrt((2 * Wind) + 0.25) - 0.5)
		WiECC= int((WiLC * (WiLC + 1)) / 2)
		if GoldenEggs < a:
			Acid= int(GoldenEggs * .01)
		if GoldenEggs >= a:
			Acid= int(GoldenEggs * .01)
		if GoldenEggs >= e:
			Acid= int(GoldenEggs * 0.08)
			if Acid < b:
				Acid = 0
		ALC= int(math.sqrt((2 * Acid) + 0.25) - 0.5)
		AECC= int((ALC * (ALC + 1)) / 2)
		if GoldenEggs < a:
			Electricity= int(GoldenEggs * .01)
		if GoldenEggs >= a:
			Electricity= int(GoldenEggs * .01)
		if GoldenEggs >= e:
			Electricity= int(GoldenEggs * 0.05)
			if Electricity < b:
				Electricity = 0
		eLC= int(math.sqrt((2 * Electricity) + 0.25) - 0.5)
		eLCC= int((eLC *(eLC + 1)) / 2)
		if GoldenEggs < a:
			Sound= int(GoldenEggs * .30)
		if GoldenEggs >= a:
			Sound= int(GoldenEggs * .21)
		if GoldenEggs >= e:
			Sound= int(GoldenEggs - (EECC + WECC + Fire + AECC + MECC + eLCC + WiECC))
			if Sound < b:
				Sound = 0				
		SLC= int(math.sqrt((2 * Sound) + 0.25) - 0.5)
		SLCC= int((SLC * (SLC + 1) / 2))
		
		LOGE= int(GoldenEggs - (EECC + WECC + Fire + AECC + MECC + eLCC + WiECC + SLCC))	
		
		if ELC < 32:
			while LOGE > ELC:
				ELC += 1
				LOGE -= ELC +1
				if LOGE < ELC:
					break
		EECC= int((ELC * (ELC + 1)) / 2)
		while LOGE > SLC:
			SLC += 1
			LOGE -= SLC + 1
			if LOGE < SLC:
				break
		SLCC= int((SLC * (SLC + 1) / 2))
		if WLC < 28:
			while LOGE > WLC:
				WLC += 1
				LOGE -= WLC + 1
				if LOGE < WLC:
					break
		WECC= int((WLC * (WLC + 1)) / 2)
		while LOGE > MLC:
			MLC += 1
			LOGE -= MLC + 1
			if LOGE < MLC:
				break
		MECC= int((MLC * (MLC + 1)) / 2)
		while LOGE > WiLC:
			WiLC += 1
			LOGE -= WiLC + 1
			if LOGE < WiLC:
				break
		WiECC= int((WiLC * (WiLC + 1)) / 2)
		while LOGE > ALC:
		 	ALC += 1
		 	LOGE -= ALC + 1
		 	if LOGE < ALC:
		 		break
		AECC= int((ALC * (ALC + 1)) / 2)
		while LOGE > eLC:
			eLC += 1
			LOGE -= eLC + 1
			if LOGE < eLC:
				break
		eLCC= int((eLC *(eLC + 1)) / 2)
		
		LOGE= int(GoldenEggs - (EECC + WECC + Fire + AECC + MECC + eLCC + WiECC + SLCC))
		if LOGE < 0:
			Fire= int(Fire - (LOGE * -1))
			LOGE= 0
	
		EECCS= str(EECC)
		EES= str(ELC)
		print("Earth Egg Level:" + EES)
		print("Cost:" + EECCS)
		
		WES= str(WLC)
		WECCS= str(WECC)
		print("Water Egg Level:" + WES)
		print("Cost:" + WECCS)
		
		SES= str(SLC)
		SLCCS= str(SLCC)
		print("Sound Egg Level:" + SES)
		print("Cost:" + SLCCS)
		
		FES= str(Fire)
		print("Fire Egg Level:" + FES)
		print("Cost:" + FES)
		
		MES= str(MLC)
		print("Magnetism Egg Levels:" + MES)
		MECCS= str(MECC)
		print("Cost:" + MECCS)
		
		WiES= str(WiLC)
		WiECCS= str(WiECC)
		print("Wind Egg Level:" + WiES)
		print("Cost:" + WiECCS)
		
		AES= str(ALC)
		AECCS= str(AECC)
		print("Acid Egg Level:" + AES)
		print("Cost:" + AECCS)
		
		eES= str(eLC)
		eLCCS= str(eLCC)
		print("Electricity Egg Level:" + eES)
		print("Cost:" + eLCCS)
			
		LOGES= str(LOGE)
		print("Left Over Golden Eggs:" + LOGES)
		if LOGE > 0:
			print("***Spend Left Over Golden Eggs On Fire***")
			print("************************************************************************")
	if UC.upper() == "L":
		from decimal import Decimal
		from functools import reduce
		import operator
		#Level 501-200000 Chicken Health Equa
		Farm_LvlHealth= input("Farm Level:")
		Farm_LvlHealthDeci= Decimal(Farm_LvlHealth)
		Farm_lvl501Deci= int(Farm_LvlHealthDeci)
		Farm_lvl501Range= range(501, Farm_lvl501Deci + 1)
		if Farm_LvlHealthDeci in Farm_lvl501Range:
			def PiNo(Farm_lvl501Range):
				import math
				Lvl501= []
				for i in Farm_lvl501Range:
						#i == 0
					Farm_lvl501Equa= Decimal((i - 1) / 500)
					Farm_lvl501EquaCon1= Decimal(1.145)
					Farm_lvl501EquaCon2= Decimal(0.001)
					Farm_lvl501Equa2= Decimal(Farm_lvl501Equa * Farm_lvl501EquaCon2 + Farm_lvl501EquaCon1)
					Farm_lvl501Equa2Deci= Decimal(Farm_lvl501Equa2)
						#Farm_lvlTotEqua3Cont= Decimal(1.3)
					Farm_lvl501EquaDeci= Decimal(Farm_lvl501Equa2)
					Lvl501.append(Farm_lvl501Equa2)
					Lvl501_PiNo= Decimal(reduce(operator.mul, Lvl501))
					Farm_lvl501EquaCon3= Decimal(4.2275)
					Farm_lvl501EquaCon4= Decimal(1*10**48)
					Farm_lvl501Equa3= Decimal(Farm_lvl501EquaCon3 * Farm_lvl501EquaCon4 * Lvl501_PiNo)
					Lvl501_PiNoDeci= Decimal(Farm_lvl501Equa3)
					Lvl501_PiNoDeciStr= str(Lvl501_PiNoDeci)
				print("Chicken Health at Specified Level:" +Lvl501_PiNoDeciStr)
			PiNo(Farm_lvl501Range)
		
		#Level 200001+
		if Farm_LvlHealthDeci >= 200001:
				Farm_Lvl200kCon1= Decimal(1.545)
				Farm_Lvl200kEqua= Decimal(Farm_Lvl200kCon1 ** (Farm_LvlHealthDeci - 200001))
				Farm_Lvl200kCon2= Decimal(1.240)
				Farm_Lvl200kCon3= Decimal(1*10**25409)
				Farm_Lvl200kEquaFin= Decimal(Farm_Lvl200kEqua * Farm_Lvl200kCon2 * Farm_Lvl200kCon3)
				Farm_Lvl200kFinDeci= Decimal(Farm_Lvl200kEquaFin)
				Farm_Lvl200kFinStr= str(Farm_Lvl200kFinDeci)
				print("Chicken Health at Specified Level:" + Farm_Lvl200kFinStr)
		
		#Level 141-500
		if 141 <= Farm_LvlHealthDeci <= 500:
				Farm_Lvl141Con1= Decimal(2.8583)
				Farm_Lvl141Con2= Decimal(10**27)
				Farm_Lvl141Con3= Decimal(1.145)
				Farm_Lvl141Con4= Decimal(Farm_Lvl141Con3 **(Farm_LvlHealthDeci - 140))
				Farm_Lvl141Equa= Decimal(Farm_Lvl141Con1 * Farm_Lvl141Con2 * Farm_Lvl141Con4)
				Farm_Lvl141EquaDeci= Decimal(Farm_Lvl141Equa)
				Farm_Lvl141EquaDeciStr= str(Farm_Lvl141EquaDeci)
				print("Chicken Health at Specified Level:" + Farm_Lvl141EquaDeciStr)
		
		#Level 1-140
		if Farm_LvlHealthDeci <= 140:
				Farm_Lvl1Con1= Decimal(1.55)
				Farm_Lvl1Equa= Decimal(Farm_LvlHealthDeci - 1 + Farm_Lvl1Con1**(Farm_LvlHealthDeci - 1))
				Farm_Lvl1EquaDeci= Decimal(Farm_Lvl1Equa)
				Farm_Lvl1EquaDeciStr= str(Farm_Lvl1EquaDeci)
				print("Chicken Health at Specified Level:" + Farm_Lvl1EquaDeciStr)		
	again()
import os
def again():
	calc_again= input("Do you want to calculate another thing? Y/N:")	
	if calc_again.upper() == "Y":
		if(os.name == "posix"):
			os.system("clear")
		else:
			os.system("cls")
		print("************************************************************************")
		calculate()
	elif calc_again.upper() == "N":
		print("Good Bye!")
		os.system("cls")
	else:
		again()
		
calculate()
