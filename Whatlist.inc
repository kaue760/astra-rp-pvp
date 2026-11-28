// Sistema Whatlist (extraido do include escondido do Santa Group)
#define WtPATHx "Whatlist"
#define WtDiagCentral   5772
#define WtQntsAcertos   15
#define WtQntsPguntas   20
#define WtSEgsPraRspd   15
enum wTInfpg{
Wt_AltCort,
Wt_Nome[128],
Wt_Pgt1[128],
Wt_Pgt2[128],
Wt_Pgt3[128],
Wt_Pgt4[128],
};
forward Wt_Delykick(playerid);
public Wt_Delykick(playerid){
return Kick(playerid);
}
