// Sistema de cofres (extraido do include escondido do Santa Group)
#define Dig_CofreCentral   	   7899
#define DiagC_SelcItem  	   Dig_CofreCentral+1
#define DiagC_QuantiaPegar     Dig_CofreCentral+2
#define Cof_QntSlots   		   15
#define Cof_MaxCofres          30
new Float:Cr_PosCofres[Cof_MaxCofres][4],Cr_CofreCriado[Cof_MaxCofres],Cr_StCofres[Cof_MaxCofres];
new cT_AddRoubCofre[MAX_PLAYERS],cT_xTKillROUBcOF[MAX_PLAYERS];
enum pInfCofres{
ID_Item,
Quantidade,
}
new Cr_yCofreDf[Cof_QntSlots][pInfCofres][Cof_MaxCofres];
new PorCofr_Plys[4][MAX_PLAYERS],Cr_pObjCofre[Cof_MaxCofres],Text3D:Cr_TxtLbcofre[Cof_MaxCofres];
new const Cf_InfoNomeItem[][] ={
"Vazio",
"Soco ingl\xEA;s",
"Taco de golf",
"Cacetete",
"Faca",
"Taco de Baseball",
"Pa",
"Taco sinuca",
"Katana",
"Serra",
"Dildo",
"Dildo",
"Dildo",
"Dildo",
"Flor",
"Bengala",
"Granada",
"Granada Fuma\xE7;a",
"Granada Fogo",
"","","",
"9mm",
"Pistola com silenciador",
"Desert Eagle",
"12 Shotgun",
"12 Cano serrado",
"12 Automatica",
"Mac 10",
"Mp5",
"Ak47",
"M4A1",
"Tec 9",
"Espingarda",
"Sniper Rifle",
"Rpg Bazuca",
"Bazuca",
"Taca Fogo",
"Mini Gun",
"Detonador",
"Spray",
"Extintor",
"Camera",
"NightVision1",
"NightVision2",
"Paraquedas",
"Dinheiro",
"Colete"
};
forward Cr_Save_Cofre(cofreid);
public Cr_Save_Cofre(cofreid){
new string[64],StrLoc[64];
format(StrLoc, sizeof(StrLoc), "Cofres/%i.ini",cofreid);
if(!DOF2_FileExists(StrLoc)) DOF2_CreateFile(StrLoc);
for(new i = 0; i < Cof_QntSlots; i++){
format(string, sizeof(string), "%i_Qnt_Slot%i", cofreid,i);
DOF2_SetInt(StrLoc,string,Cr_yCofreDf[i][Quantidade][cofreid]);
format(string, sizeof(string), "%i_ID_Slot%i", cofreid,i);
DOF2_SetInt(StrLoc,string,Cr_yCofreDf[i][ID_Item][cofreid]);
}
DOF2_SaveFile();
return 1;
}
forward Cr_Load_Cofre(cofreid);
public Cr_Load_Cofre(cofreid){
new string[64],StrLoc[64];
format(StrLoc, sizeof(StrLoc), "Cofres/%i.ini", cofreid);
Cr_CofreCriado[cofreid] = DOF2_GetInt(StrLoc,"Orgid");
if(Cr_CofreCriado[cofreid] != 0){
Cr_PosCofres[cofreid][0] = DOF2_GetFloat(StrLoc,"Pos_X");
Cr_PosCofres[cofreid][1] = DOF2_GetFloat(StrLoc,"Pos_Y");
Cr_PosCofres[cofreid][2] = DOF2_GetFloat(StrLoc,"Pos_Z");
Cr_PosCofres[cofreid][3] = DOF2_GetFloat(StrLoc,"Pos_A");
for(new i = 0; i < Cof_QntSlots; i++){
format(string, sizeof(string), "%i_Qnt_Slot%i", cofreid,i);
Cr_yCofreDf[i][Quantidade][cofreid] = DOF2_GetInt(StrLoc,string);
format(string, sizeof(string), "%i_ID_Slot%i", cofreid,i);
Cr_yCofreDf[i][ID_Item][cofreid] = DOF2_GetInt(StrLoc,string);
}
}
return 1;
}
