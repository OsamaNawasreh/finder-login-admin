#!/usr/bin/env python3
import urllib.request
from optparse import OptionParser
def osama_admin(url):
    try:		
        open_url = urllib.request.urlopen(url)
        osamalist = ["admin.php","admin.html","index.php","login.php","login.html","administrator","admin","adminpanel","cpanel","login","wp-login.php","administrator","admins","logins","admin.asp","login.asp","adm/","admin/","admin/account.html","admin/login.html","admin/login.htm","admin/controlpanel.html","admin/controlpanel.htm","admin/adminLogin.html","admin/adminLogin.htm","admin.htm","admin.html","adminitem/","adminitems/","administrator/","administrator/login.%EXT%","administrator.%EXT%","administration/","administration.%EXT%","adminLogin/","adminlogin.%EXT%","admin_area/admin.%EXT%","admin_area/","admin_area/login.%EXT%","manager/","superuser/","superuser.%EXT%","access/","access.%EXT%","sysadm/","sysadm.%EXT%","superman/","supervisor/","panel.%EXT%","control/","control.%EXT%","member/","member.%EXT%","members/","user/","user.%EXT%","cp/","uvpanel/","manage/","manage.%EXT%","management/","management.%EXT%","signin/","signin.%EXT%","log-in/","log-in.%EXT%","log_in/","log_in.%EXT%","sign_in/","sign_in.%EXT%","sign-in/","sign-in.%EXT%","users/","users.%EXT%","accounts/","accounts.%EXT%","bb-admin/login.%EXT%","bb-admin/admin.%EXT%","bb-admin/admin.html","administrator/account.%EXT%","relogin.htm","relogin.html","check.%EXT%","relogin.%EXT%","blog/wp-login.%EXT%","user/admin.%EXT%","users/admin.%EXT%","registration/","processlogin.%EXT%","checklogin.%EXT%","checkuser.%EXT%","checkadmin.%EXT%","isadmin.%EXT%","authenticate.%EXT%","authentication.%EXT%","auth.%EXT%","authuser.%EXT%","authadmin.%EXT%","cp.%EXT%","modelsearch/login.%EXT%","moderator.%EXT%","moderator/","controlpanel/","controlpanel.%EXT%","admincontrol.%EXT%","adminpanel.%EXT%","fileadmin/","fileadmin.%EXT%","sysadmin.%EXT%","admin1.%EXT%","admin1.html","admin1.htm","admin2.%EXT%","admin2.html","yonetim.%EXT%","yonetim.html","yonetici.%EXT%","yonetici.html","phpmyadmin/","myadmin/","ur-admin.%EXT%","ur-admin/","Server.%EXT%","Server/","wp-admin/","administr8.%EXT%","administr8/","webadmin/","webadmin.%EXT%","administratie/","admins/","admins.%EXT%","administrivia/","Database_Administration/","useradmin/","sysadmins/","sysadmins/","admin1/","system-administration/","administrators/","pgadmin/","directadmin/","staradmin/","ServerAdministrator/","SysAdmin/","administer/","LiveUser_Admin/","sys-admin/","typo3/","panel/","cpanel/","cpanel_file/","platz_login/","rcLogin/","blogindex/","formslogin/","autologin/","manuallogin/","simpleLogin/","loginflat/","utility_login/","showlogin/","memlogin/","login-redirect/","sub-login/","wp-login/","login1/","dir-login/","login_db/","xlogin/","smblogin/","customer_login/","UserLogin/","login-us/","bigadmin/","project-admins/","phppgadmin/","pureadmin/","pureadmin/","sql-admin/","radmind/","openvpnadmin/","wizmysqladmin/","vadmind/","ezsqliteadmin/","newsadmin/","adminpro/","Lotus_Domino_Admin/","bbadmin/","vmailadmin/","Indy_admin/","ccp14admin/","banneradmin/","sshadmin/","phpldapadmin/","macadmin/","administratoraccounts/","admin4_account/","admin4_colon/","Super-Admin/","AdminTools/","cmsadmin/","SysAdmin2/","globes_admin/","cadmins/","phpSQLiteAdmin/","navSiteAdmin/","server_admin_small/","logo_sysadmin/","power_user/","system_administration/","ss_vms_admin_sm/","bb-admin/","panel-administracion/","instadmin/","memberadmin/","administratorlogin/","adm.%EXT%","admin_login.%EXT%","panel-administracion/login.%EXT%","pages/admin/admin-login.%EXT%","pages/admin/","acceso.%EXT%","admincp/login.%EXT%","admincp/","adminarea/","admincontrol/","affiliate.%EXT%","adm_auth.%EXT%","memberadmin.%EXT%","administratorlogin.%EXT%","modules/admin/","administrators.%EXT%","siteadmin/","siteadmin.%EXT%","adminsite/","kpanel/","vorod/","vorod.%EXT%","vorud/","vorud.%EXT%","adminpanel/","PSUser/","secure/","webmaster/","webmaster.%EXT%","autologin.%EXT%","userlogin.%EXT%","admin_area.%EXT%","cmsadmin.%EXT%","security/","usr/","root/","secret/","admin/login.%EXT%","admin/adminLogin.%EXT%","moderator.php","moderator.html","moderator/login.%EXT%","moderator/admin.%EXT%","yonetici.%EXT%","0admin/","0manager/","aadmin","cgi-bin/login%EXT%","login1%EXT%","login_admin/","login_admin%EXT%","login_out/","login_out%EXT%","login_user%EXT%","loginerror/","loginok/","loginsave/","loginsuper/","loginsuper%EXT%","login%EXT%","logout/","logout%EXT%","secrets/","super1/","super1%EXT%","super_index%EXT%","super_login%EXT%","supermanager%EXT%","superman%EXT%","superuser%EXT%","supervise/","supervise/Login%EXT%","super%EXT%"]
        for i in osamalist:
            i = i.rstrip("\n")
            test = url+""+i
            try:
            	open_url = urllib.request.urlopen(test)
            	print(test+" :: found [+]")
            except urllib.error.HTTPError as msg:
            	print(test+" :: Not found [-]")
            	print(msg)
    except urllib.error.URLError as msg:
        print(url)
        print(msg)
nawasreh = OptionParser("""
------------------------------------------------------------------------
------------------------------------------------------------------------                            
https://github.com/OsamaNawasreh/

https://www.instagram.com/os66a12/

                    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠
                    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ 
                            ☢ ☣ ☢ ☣ ☢ ☣ ☢ ☣ ☢ ☣ 
                    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠                 
                    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠
                       
                              hacker osama Nawasreh
-------------------------------------------------------------------------
-------------------------------------------------------------------------
python3 finder-login-admin.py -u or url url+/
 
 is important     url + /
--------------

ex:
python3 finder-login-admin.py -u http://testphp.vulnweb.com/
python3 finder-login-admin.py --url https://www.yahoo.com/


    """)
nawasreh.add_option("-u","--url",dest="s_url",type="string",help="plz url")
(options ,args) = nawasreh.parse_args()
if options.s_url == None:
    print(nawasreh.usage)
else:
    osama_admin(options.s_url)
