
<!--
<br>

<details>
<summary>支持的漏洞列表 [点击展开] </summary>  
-->

| 应用                        | 漏洞名称                                                            | POC路径                                                                      |
|---------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------|
| 360                       | 360天擎数据库未授权访问                                                   | ``poc/360/TianQing_Unauth_Acceess/poc.py``                                 |
|                           | 360天擎前台SQL注入                                                    | ``poc/360/TianQing_SQLi/poc.py``                                           |
| ACME                      | mini_httpd任意文件读取漏洞(CVE-2018-18778)                              | ``poc/ACME/File_Read_mini_httpd_CVE_2018_18778/poc.py``                    |
| AJ_Report                 | AJ-Report 身份验证绕过和远程代码执行 (CNVD-2024-15077)                       | ``poc/AJ_Report/RCE_CNVD_2024_15077/poc.py``                               |
| Alibaba_Alist             | AList云盘 未授权访问                                                   | ``poc/Alibaba_Alist/UnAuth_Access/poc.py``                                 |
| Alibaba_Canal             | Alibaba Canal 默认弱口令漏洞                                           | ``poc/Alibaba_Canal/Weak_Pass/poc.py``                                     |
|                           | Alibaba Canal 信息泄露                                              | ``poc/Alibaba_Canal/Info_Disclosure/poc.py``                               |
| Alibaba_Druid             | Druid未授权访问                                                      | ``poc/Alibaba_Druid/Unauth_Access/poc.py``                                 |
| Alibaba_Fastjson          | Fastjson 反序列化远程代码执行漏洞（CVE-2017-18349）                           | ``poc/Alibaba_FastJson/RCE_CVE_2017_18349/poc.py``                         |
| Alibaba_Nacos             | Nacos未授权访问                                                      | ``poc/Alibaba_Nacos/Unauth_Access/poc.py``                                 |
| Apache ActiveMQ           | Apache ActiveMQ 远程代码执行漏洞(CVE-2016-3088)                         | ``poc/Apache_ActiveMQ/RCE_FileServer_CVE_2016_3088/poc.py``                |
|                           | Apache ActiveMQ 弱口令 ➕ CVE-2015-5254                             | ``poc/Apache_ActiveMQ/WeakPass/poc.py``                                    |
|                           | ActiveMQ物理路径泄漏漏洞                                                | ``poc/Apache_ActiveMQ/Physical_Path_Disclosure/poc.py``                    |
| Apache_ApiSix             | Apache APISIX Dashboard 身份验证绕过漏洞（CVE-2021-45232）                | ``poc/Apache_ApiSix/DashBoard_Auth_Bypass_CVE_2021_45232/poc.py``          |
|                           | Apache APISIX batch-requests 未授权RCE(CVE-2022-24112)             | ``poc/Apache_ApiSix/RCE_CVE_2022_24112/poc.py``                            |
|                           | Apache APISIX 默认密钥漏洞（CVE-2020-13945）                            | ``poc/Apache_ApiSix/Default_Key_CVE_2020_13945/poc.py``                    |
| Apache CouchDB            | Apache Couchdb 远程权限提升(CVE-2017-12635)                           | ``poc/Apache_CouchDB/Priv_Escalation_CVE-2017_12635/poc.py``               |
| Apache Druid              | Apache Druid任意文件读取复现(CVE-2021-36749)                            | ``poc/Apache_Druid/File_Read_CVE_2021_36749/poc.py``                       |
|                           | Apache Druid 远程代码执行漏洞 (CVE-2021-25646)                          | ``poc/Apache_Druid/RCE_CVE_2021_25646/poc.py``                             |
| Apache Flink              | Apache Flink目录穿透(CVE-2020-17519)                                | ``poc/Apache_Flink/Dir_Traversal_CVE_2020_17519/poc.py``                   |
|                           | Apache Flink <= 1.9.1远程代码执行 CVE-2020-17518                      | ``poc/Apache_Flink/RCE_CVE_2020_17518/poc.py``                             |
| Apache_Hadoop             | Apache Hadoop反序列化漏洞(CVE-2021-25642)                             | ``poc/Apache_Hadoop/RCE_CVE_2021_25642/poc.py``                            |
| Apache Kylin              | Apache Kylin 未授权配置泄露 CVE-2020-13937                             | ``poc/Apache_Kylin/Conf_Info_Disclosure_CVE_2020_13937/poc.py``            |
| Apache Mod_jk             | Apache Mod_jk 访问控制权限绕过(CVE-2018-11759)                          | ``poc/Apache_Mod_jk/ACbypass_CVE_2018_11759/poc.py``                       |
| Apache Shiro              | Shiro 1.2.4 反序列化漏洞                                              | ``poc/Apache_Shiro/RCE_CVE_2016_4437/poc.py``                              |
|                           | Shiro指纹识别                                                       | ``poc/Apache_Shiro/FingerPrint/poc.py``                                    |
| Apache Solr               | Apache Solr Velocity 注入远程命令执行漏洞 (CVE-2019-17558)                | ``poc/Apache_Solr/CVE_2019_17558/poc.py``                                  |
|                           | Apache Solr 任意文件读取漏洞                                            | ``poc/Apache_Solr/File_Read/poc.py``                                       |
|                           | Apache Solr 远程命令执行 Log4j                                        | ``poc/Apache_Solr/RCE_Log4j_CVE_2021_44228/poc.py``                        |
| Apache ZooKeeper          | ZooKeeper未授权访问                                                  | ``poc/Apache_ZooKeeper/Unauth_Access/poc.py``                              |
| 碧海威 L7                    | 碧海威 L7 弱口令漏洞                                                    | ``poc/Bithighway_碧海威/Weak_Pass_L7/poc.py``                                 |
| BSPHP                     | BSPHP 未授权访问 信息泄露漏洞                                              | ``poc/BSPHP/Info_Disclosure/poc.py``                                       |
| C-Lodop                   | C-Lodop 云打印机系统平台任意文件读取漏洞                                        | ``poc/C_Lodop/File_Read/poc.py``                                           |
| 中国电信                      | 电信天翼网关F460 web_shell_cmd.gch 远程命令执行漏洞                           | ``poc/China_TeleCOM_中国电信/RCE_F460_GateWay/poc.py``                         |
|                           | 大唐电信AC集中管理平台默认口令                                                | ``poc/China_TeleCOM_中国电信/Weak_Pass_DaTang_AC_Manager/poc.py``              |
| 中国移动                      | 中国移动 禹路由 ExportSettings.sh 敏感信息泄露漏洞                             | ``poc/China_Mobile_中国移动/Info_Disclosure_Yu_routing_ExportSettings/poc.py`` |
| CmsEasy                   | CmsEasy crossall_act.php SQL注入漏洞                                | ``poc/CmsEasy/SQLi_CrossAllAct_php/poc.py``                                |
| common(通用)                | git信息泄露                                                         | ``poc/common/Git_Info_Disclosure/poc.py``                                  |
|                           | svn信息泄露                                                         | ``poc/common/Svn_Info_Disclosure/poc.py``                                  |
|                           | URL存活检测                                                         | ``poc/common/Url_Alive/poc.py``                                            |
|                           | Apache列目录                                                       | ``poc/common/Apache_Dir_List/poc.py``                                      |
|                           | 备份泄露/源码泄露                                                       | ``poc/common/CodeDisclosure/poc.py``                                       |
| Confluence                | Confluence Server Webwork OGNL注入 PreAuth-RCE(CVE-2021-26084)    | ``poc/Confluence/OGNL_Injection_CVE_2021_26084/poc.py``                    |
|                           | Atlassian Confluence OGNL表达式注入漏洞（CVE-2022-26134）                | ``poc/Confluence/OGNL_Injection_CVE_2022_26134/poc.py``                    |
|                           | Confluence 路径穿越与命令执行（CVE-2019-3396）                             | ``poc/Confluence/Path_Travel_CVE_2019_3396/poc.py``                        |
| Coremail                  | Coremail 配置信息泄露漏洞                                               | ``poc/Coremail/Conf_Info_Disclosure/poc.py``                               |
| 赤兔CMS                     | 赤兔CMS banner识别插件                                                | ``poc/CtCMS_赤兔CMS/Get_Banner/poc.py``                                      |
| D-Link                    | D-Link ShareCenter DNS-320 system_mgr.cgi 远程命令执行漏洞              | ``poc/D_Link/RCE_ShareCenter_system_mgr_cgi/poc.py``                       |
|                           | D-Link Dir-645 getcfg.php 账号密码泄露漏洞(CVE-2019-17506)              | ``poc/D_Link/UPInfo_Disclosure_getcfg_php/poc.py``                         |
|                           | D-Link AC管理系统默认账号密码                                             | ``poc/D_Link/Weak_Pass_AC_Manager/poc.py``                                 |
| Dapr                      | Dapr Dashboard未授权访问(CVE-2022-38817)                             | ``poc/Dapr/Unauth_Access_DashBoard/poc.py``                                |
| DBAppSecurity 安恒信息        | 明御WAF登陆绕过                                                       | ``poc/dbappsecurity_安恒信息/Login_ByPass_MingYu_WAF/poc.py``                  |
| 织梦CMS                     | 织梦CMS radminpass.php文件暴露                                        | ``poc/DedeCMS_织梦/RadminPass/poc.py``                                       |
|                           | DedeCMS 短文件名信息泄露                                                | ``poc/DedeCMS_织梦/Info_Disclosure_IIS_Short_Filename/poc.py``               |
| DocCMS                    | DocCMS keyword SQL注入漏洞                                          | ``poc/DocCMS/SQLi_keyword/poc.py``                                         |
| Docker                    | Docker Remote API未授权访问                                          | ``poc/Docker/Unauth_Remote_Api/poc.py``                                    |
| DrayTek                   | DrayTek企业网络设备 远程命令执行(CVE-2020-8515)                             | ``poc/DrayTek/RCE_CVE_2020_8515/poc.py``                                   |
| Drupal!                   | Drupal!远程代码执行(CVE-2018-7600)                                    | ``poc/Drupal!/RCE_CVE_2018_7600/poc.py``                                   |
| DVR                       | DVR登录绕过漏洞(CVE-2018-9995)                                        | ``poc/DVR/Login_Bypass_CVE_2018_9995/poc.py``                              |
| ECShop                    | ECShop 4.1.0前台 delete_cart_goods.php SQL注入(CNVD-2020-58823)     | ``poc/ECShop/SQLi_delete_cart_goods/poc.py``                               |
|                           | ECShop 2.x/3.x SQL 注入/远程代码执行漏洞                                  | ``poc/ECShop/RCE_2dotX_OR_3dotX/poc.py``                                   |
| ElasticSearch             | ElasticSearch 未授权访问                                             | ``poc/Elasticsearch/Unauth_Access/poc.py``                                 |
|                           | ElasticSearch 命令执行漏洞（CVE-2014-3120）                             | ``poc/Elasticsearch/Cmd_Exec_MVEL_CVE-2014-3120/poc.py``                   |
|                           | ElasticSearch Groovy 沙盒绕过 && 代码执行漏洞（CVE-2015-1427）              | ``poc/Elasticsearch/Code_Exec_Groovy_CVE-2015-1427/poc.py``                |
|                           | ElasticSearch 目录穿越漏洞（CVE-2015-5531）                             | ``poc/Elasticsearch/Dir_Traversal_CVE-2015-5531/poc.py``                   |
|                           | Elasticsearch写任意文件漏洞（WooYun-2015-110216）                        | ``poc/Elasticsearch/File_Create_WooYun-2015-110216/poc.py``                |
| EnjoySCM_捷诚               | EnjoySCM UploadFile任意文件上传漏洞                                     | ``poc/EnjoySCM_捷诚/FileUpload_UploadFile/poc.py``                           |
| Eyou 亿邮电子邮件系统             | 亿邮电子邮件系统 远程命令执行                                                 | ``poc/Eyou_亿邮/RCE_moni_detail/poc.py``                                     |
| F5                        | F5 BIG-IP任意文件读取(CVE-2020-5902)                                  | ``poc/F5_BIG_IP/File_Read_CVE_2020_5902/poc.py``                           |
|                           | CVE-2021-22986 RCE                                              | ``CVE-2021-22986 RCE``                                                     |
| FineReport_帆软             | 帆软报表 V8 get_geo_json 任意文件读取漏洞                                   | ``poc/FineReport_帆软/FileRead8/poc.py``                                     |
| 菲力尔                       | FLIR-AX8 download.php 任意文件下载                                    | ``poc/FLIR_菲力尔/Download_File_AX8/poc.py``                                  |
| Fortinet_美国飞塔             | 飞塔(Fortinet)防火墙身份认证绕过漏洞(CVE-2022-40684)                         | ``poc/Fortinet_美国飞塔/Authentication_Bypass_FortiOS_CVE_2022_40648/poc.py``  |
|                           | Fortigate SSL VPN fgt_lang 任意文件读取                               | ``poc/Fortinet_美国飞塔/FileRead_SSL_VPN/poc.py``                              |
| FTP                       | FTP匿名访问                                                         | ``poc/FTP/Anonymous_Access/poc.py``                                        |
| GeoServer                 | CVE-2024-36401 未授权RCE                                           | `poc/GeoServer/RCE_CVE_2024_36401/poc.py`                                  |
| Grafana                   | Grafana plugins 任意文件读取漏洞(CVE-2021-43798)                        | ``poc/Grafana/File_Read_plugins/poc.py``                                   |
| H2 数据库                    | H2 数据库 Web控制台未授权访问                                              | ``poc/H2_DataBase/UnAuth_Access/poc.py``                                   |
| H3C SecPath 下一代防火墙        | H3C SecPath 下一代防火墙 任意文件下载漏洞                                     | ``poc/H3C/File_Download_SecPath_WAF/poc.py``                               |
| HanWang 汉王                | 汉王e脸通综合管理平台 queryManyPeopleGroupList接口SQL注入                     | `poc/HanWang/SQLi_queryManyPeopleGroupList/poc.py`                         |
|                           | 汉王e脸通综合管理平台 getGroupEmployee SQL注入                              | `poc/HanWang/SQLi_getGroupEmployee/poc.py`                                 |
| 海康威视                      | HIKVISION 视频编码设备接入网关 任意文件下载                                     | ``poc/HIKVISION/File_Down_Gateway_downFile_php/poc.py``                    |
|                           | HIKVISION 流媒体管理服务器弱口令                                           | ``poc/HIKVISION/Weak_Pass_Stream_Media_Manager/poc.py``                    |
|                           | HIKVISION 流媒体管理服务器任意文件读取                                        | ``poc/HIKVISION/File_Read_Stream_Media_Manager/poc.py``                    |
|                           | 海康威视 IP摄像头未授权访问（CVE-2017-7921）                                  | ``poc/HIKVISION/UnAuth_Access_CVE_2017_7921/poc.py``                       |
|                           | HIKVISION 综合安防管理平台 applyCT Fastjson远程命令执行漏洞                     | ``poc/HIKVISION/RCE_applyCT_FastJson/poc.py``                              |
|                           | 海康威视 IP Camera 远程命令执行漏洞（CVE-2021-36260）                         | ``poc/HIKVISION/RCE_IP_Camera_CVE_2021_36260/poc.py``                      |
| 宏电                        | 宏电 H8922 后台任意文件读取漏洞                                             | ``poc/Hongdian_宏电/Backstage_File_Read_CVE_2021_28152/poc.py``              |
| 好视通                       | 好视通视频会议平台 任意文件下载                                                | ``poc/HST_好视通/File_Download/poc.py``                                       |
| 华天动力                      | 华天动力OA 8000版 workFlowService SQL注入漏洞                            | `poc/HT_华天动力OA/SQLi_workFlowService/poc.py`                                |
| 华为                        | Huawei HG659 lib 任意文件读取漏洞                                       | ``poc/Huawei/File_Read_HG659_lib/poc.py``                                  |
|                           | 华为路由器敏感信息泄露 DG8045 Router 1.0                                   | ``poc/Huawei/Info_Disclosure_DG8045/poc.py``                               |
| 华域                        | 华域Reporter组件 命令注入漏洞                                             | `poc/HuaYuLab/Cmd_inj_Report/poc.py`                                       |
| 汇文                        | 汇文OPAC敏感信息泄露                                                    | ``poc/HuiWen_汇文/Info_Disclosure/poc.py``                                   |
|                           | 汇文OPAC弱口令                                                       | ``poc/HuiWen_汇文/Weak_Pass/poc.py``                                         |
| 蜂网互联                      | 蜂网互联 企业级路由器v4.31 密码泄露漏洞                                         | ``poc/IFW8_蜂网互联/UPInfo_DisClosure_CVE_2019_16313/poc.py``                  |
| 爱快                        | iKuai路由器 login/user处sql注入                                       | `poc/iKuai8_爱快/SQLi_Login_user/poc.py`                                     |
| InfluxDB                  | InfluxDB指纹识别                                                    | ``poc/InfluxDB/FingerPrint/poc.py``                                        |
|                           | InfluxDB 未授权访问                                                  | ``poc/InfluxDB/UnAuth_Access/poc.py``                                      |
| 红帆                        | 红帆OA ioFileExport.aspx 任意文件读取漏洞                                 | `poc/ioffice_红帆/FileRead_ioFileExport_aspx/poc.py`                         |
| Intelbras                 | Intelbras Wireless 未授权与密码泄露                                     | ``poc/Intelbras/UPInfo_Disclosure_CVE_2021_3017/poc.py``                   |
| Jboss                     | Jboss未授权访问                                                      | ``poc/Jboss/Unauth_Access/poc.py``                                         |
| Jellyfin                  | Jellyfin任意文件读取                                                  | ``poc/jellyfin/File_Read_CVE_2021_21402/poc.py``                           |
|                           | Jellyfin RemoteImageController.cs SSRF漏洞(CVE-2021-29490)        | ``poc/jellyfin/SSRF_CVE_2021_29490/poc.py``                                |
| Jenkins                   | Jenkins未授权访问                                                    | ``poc/Jenkins/Unauth_Access/poc.py``                                       |
| Jetty                     | Jetty WEB-INF文件读取漏洞(CVE-2021-34429)                             | ``poc/Jetty/File_Read_CVE_2021_34429/poc.py``                              |
|                           | Jetty指纹识别                                                       | ``poc/Jetty/FingerPrint/poc.py``                                           |
|                           | Jetty WEB-INF 敏感信息泄露漏洞（CVE-2021-28164）                          | ``poc/Jetty/Info_Disclosure_CVE_2021_28164/poc.py``                        |
|                           | Jetty Utility Servlets ConcatServlet 双解码信息泄露漏洞 (CVE-2021-28169) | ``poc/Jetty/Info_Disclosure_CVE_2021_28169/poc.py``                        |
| JimuReport                | JimuReport FreeMarker 服务端模板注入命令执行（CVE-2023-4450）                | ``poc/JimuReport/RCE_CVE_2023_4450/poc.py``                                |
| 金和OA                      | 金和OA C6 download.jsp 任意文件读取漏洞                                   | ``poc/Jinher_金和OA/File_Read_download_jsp/poc.py``                          |
| Joomla                    | Joomla！Rest api 信息泄露（CVE-2023-23752）                            | `poc/Joomla!/Info_Disclosure_CVE_2023_23752/poc.py`                        |
|                           | Joomla! 未授权访问漏洞(CVE-2023-23752)                                 | `poc/Joomla!/UnAuthAccess_CVE_2023_23752/poc.py`                           |
| KEDACOM 数字系统接入网关          | KEDACOM 数字系统接入网关 任意文件读取漏洞                                       | ``poc/KEDACOM_数字系统接入网关/File_Read/poc.py``                                  |
| 金蝶OA                      | 金蝶协同办公系统 fileDownload.do 任意文件下载漏洞                               | ``poc/Kingdee_金蝶/File_Down_fileDownload_do/poc.py``                        |
|                           | 金蝶OA server_file 目录遍历漏洞                                         | ``poc/Kingdee_金蝶/Dir_List_server_file/poc.py``                             |
| Kyan网络监控设备                | Kyan网络监控设备信息泄露                                                  | ``poc/Kyan/Info_Disclosure/poc.py``                                        |
| 蓝凌OA                      | 蓝凌OA custom.jsp 前台任意文件读取漏洞                                      | ``poc/Landray_蓝凌OA/File_Read_CNVD_2021_28277/poc.py``                      |
|                           | 蓝凌OA treexml.tmpl脚本 远程命令执行                                      | ``poc/Landray_蓝凌OA/RCE_TreeXmlTMPL_Script/poc.py``                         |
|                           | 蓝凌OA sysFormulaSimulateByJS 未授权命令执行漏洞                           | ``poc/Landray_蓝凌OA/RCE_sysFormulaSimulateByJS/poc.py``                     |
| Laravel Framework         | Laravel .env 配置文件泄露                                             | ``poc/Laravel_Framework/Conf_Info_Disclosure_dot_env/poc.py``              |
| 朗驰欣创                      | 朗驰欣创视频监控系统 FTP账号密码泄露                                            | ``poc/LinkSeek_朗驰欣创/FTP_Account_Info_Disclosure/poc.py``                   |
| 利谱第二代防火墙                  | 利谱第二代防火墙存在信息泄露漏洞                                                | ``poc/LiPu_利谱第二代防火墙/Info_Disclosure/poc.py``                               |
| 佑友                        | 佑友防火墙 弱口令                                                       | ``poc/MailGard_佑友/Weak_Pass_FireWall/poc.py``                              |
|                           | 佑友防火墙 后台命令执行漏洞                                                  | ``poc/MailGard_佑友/RCE_ping_FireWall/poc.py``                               |
| 迈普 ISG1000安全网关            | 迈普 ISG1000安全网关 任意文件下载漏洞                                         | ``poc/MaiPu_迈普/File_Download_webui/poc.py``                                |
| MemCache                  | MemCache未授权访问                                                   | ``poc/MemCache/UnAuth_Access/poc.py``                                      |
| MessageSolution企业邮件归档管理系统 | MessageSolution企业邮件归档管理系统 EEA 信息泄露                              | ``poc/MessageSolution/Info_Disclosure/poc.py``                             |
| MetaBase                  | MetaBase任意文件读取漏洞 CVE-2021-41277                                 | ``poc/Metabase/File_Read_CVE_2021_41277/poc.py``                           |
|                           | CVE-2023-38646 Metabase RCE                                     | `poc/Metabase/RCE_CVE_2023_38646/poc.py`                                   |
| MetInfo                   | MetInfo任意文件读取漏洞                                                 | `poc/MetInfo/FileRead_thumb/poc.py`                                        |
| MicroSoft                 | Windows HTTP协议栈远程代码执行漏洞(CVE-2022-21907)                         | poc/MicroSoft/RCE_CVE_2022_21907/poc.py                                    |
| MongoDB                   | MongoDB未授权访问                                                    | ``poc/MongoDB/Unauth_Access/poc.py``                                       |
| Mysql                     | Mysql弱口令                                                        | ``poc/Mysql/WeakPass/poc.py``                                              |
| 蓝海卓越                      | 蓝海卓越计费管理系统 任意文件读取                                               | ``poc/NatShell_蓝海卓越/File_Read/poc.py``                                     |
|                           | 蓝海卓越计费管理系统 认证hash泄露                                             | ``poc/NatShell_蓝海卓越/HashInfo_DisClosure/poc.py``                           |
| 网康                        | 网康下一代防火墙 checkProcessNumber 远程命令执行                              | `poc/NetentSec_网康/RCE_checkProcessNumber/poc.py`                           |
|                           | 网康下一代防火墙 doSetStatus 反序列化RCE                                    | `poc/NetentSec_网康/RCE_doSetStatus/poc.py`                                  |
|                           | 网康下一代防火墙 version参数 前台RCE                                        | `poc/NetentSec_网康/RCE_Version/poc.py`                                      |
| 中科网威                      | 中科网威 下一代防火墙控制系统 账号密码泄露漏洞                                        | ``poc/NetPower_中科网威/UPInfo_DisClosure_Firewall/poc.py``                    |
| Nexus                     | Nexus Repository Manager 3 远程命令执行漏洞（CVE-2019-7238）              | `poc/Nexus/RCE_CVE_2019_7238/poc.py`                                       |
| Node.js                   | Node.js目录穿越漏洞                                                   | ``poc/Node.js/Dir_Traversal_CVE_2017_14849/poc.py``                        |
|                           | Node.js命令注入漏洞（CVE-2021-21315）                                   | ``poc/Node.js/Cmd_inj_CVE_2021_21315/poc.py``                              |
| 绿盟                        | 绿盟下一代防火墙 resourse.php 任意文件上传漏洞                                  | ``poc/nsfocus_绿盟/File_upload_NF/poc.py``                                   |
| 新软科技                      | 极通EWEBS应用虚拟化系统任意文件读取                                            | ``poc/NSoft_新软/FileRead_EWEBS/poc.py``                                     |
| OKI                       | OKI MC573未授权访问                                                  | ``poc/OKI/UnAuth_MC573/poc.py``                                            |
| 梨子项目管理系统                  | 梨子项目管理系统 信息泄露漏洞                                                 | ``poc/PearProject_梨子项目管理系统/Conf_Info_Disclosure_env/poc.py``               |
| PHP                       | php v8.1开发版后门检测                                                 | ``poc/php/Backdoor_v8dev/poc.py``                                          |
| PHPStudy                  | PHPStudy 后门检测                                                   | ``poc/PHPStudy/Back_Door/poc.py``                                          |
| PHPUnit                   | PHPUnit eval-stdin.php 远程命令执行漏洞                                 | ``poc/PHPUnit/RCE_eval_stdin/poc.py``                                      |
| QZSec_齐治                  | 齐治堡垒机 任意用户登录漏洞                                                  | ``poc/QZSec_齐治/AnyUser_Login_Fortress_Machine/poc.py``                     |
| Redis                     | Redis未授权访问                                                      | ``poc/Redis/Unauth_Access/poc.py``                                         |
|                           | Redis Lua 沙箱逃逸和远程代码执行 (CVE-2022-0543)                           | ``poc/Redis/RCE_Lua_Sandbox_Escape_CVE_2022_0543/poc.py``                  |
| RLM                       | Reprise License Manager 14.2 信息泄露（CVE-2022-28365）               | ``poc/RLM/Info_Disclosure_CVE_2022_28365/poc.py``                          |
| 锐捷                        | 锐捷EG网关 userAuth.php存在任意文件读取漏洞                                   | ``poc/Ruijie_锐捷/File_Read_EG_userAuth/poc.py``                             |
|                           | 锐捷NBR 1300G 路由器 越权CLI命令执行漏洞                                     | ``poc/Ruijie_锐捷/RCE_NBR_1300G/poc.py``                                     |
|                           | 锐捷NBR路由器 EWEB网管系统 远程命令执行漏洞                                      | ``poc/Ruijie_锐捷/RCE_EWEB_Manager_CNVD_2021_09650/poc.py``                  |
|                           | 锐捷RG-UAC/RG-ISG统一上网行为管理审计系统存在账号密码信息泄露                           | ``poc/Ruijie_锐捷/UPInfo_DisClosure_RG_UAC_CNVD_2021_14536/poc.py``          |
|                           | 锐捷Smartweb管理系统 默认账户➕命令执行漏洞                                      | ``poc/Ruijie_锐捷/RCE_SmartWeb_WEB_VMS/poc.py``                              |
|                           | 锐捷云课堂主机 目录遍历漏洞                                                  | ``poc/Ruijie_锐捷/Dir_List_Cloud_ClassRoom/poc.py``                          |
| 若依后台管理系统                  | 若依后台管理系统 弱口令                                                    | ``poc/RuoYi_若依/Weak_Pass/poc.py``                                          |
| Samsung                   | 三星路由器本地文件包含                                                     | ``poc/Samsung/Lfi_Samsung_Wlan_AP/poc.py``                                 |
|                           | 三星 WLAN AP WEA453e路由器 远程命令执行漏洞                                  | ``poc/Samsung/RCE_Samsung_WLANAP_WEA453e/poc.py``                          |
| Sangfor 深信服               | 深信服EDR终端检测响应平台RCE漏洞(CNVD-2020-46552)                            | ``poc/SANGFOR_深信服/RCE_2020_EDR/poc.py``                                    |
| Sapido                    | Sapido BRC70n路由器远程代码执行漏洞                                        | ``poc/Sapido/RCE_BRC70n_Router/poc.py``                                    |
| 致远OA                      | 致远OA webmail.do 任意文件下载 (CNVD-2020-62422)                        | ``poc/SeeYon_致远/File_Download/poc.py``                                     |
|                           | 致远OA ajax.do 任意文件上传                                             | ``poc/SeeYon_致远/File_Upload_ajax_do/poc.py``                               |
|                           | 致远OA getSessionList.jsp Session泄漏漏洞                             | ``poc/SeeYon_致远/Session_Disclosure_getSessionList/poc.py``                 |
|                           | 致远OA A6 test.jsp SQL注入漏洞                                        | ``poc/SeeYon_致远/SQLi_test_jsp/poc.py``                                     |
|                           | Sophos Mobile OmaDsServlet XML实体注入(CVE-2022-3980)               | ``poc/Sophos/XXE_CVE_2022_3980/poc.py``                                    |
| 狮子鱼CMS                    | 狮子鱼CMS ApiController.class.php SQL注入漏洞                          | ``poc/ShiZiYu_狮子鱼/Sqli_ApiController/poc.py``                              |
|                           | 狮子鱼CMS ApigoodsController.class.php SQL注入漏洞                     | ``poc/ShiZiYu_狮子鱼/Sqli_ApigoodsController/poc.py``                         |
| ShopXO                    | ShopXO download 任意文件读取漏洞(CNVD-2021-15822)                       | ``poc/ShopXO/FileRead_CNVD_2021_15822/poc.py``                             |
| SonarQube                 | SonarQube api 信息泄露漏洞                                            | ``poc/SonarQube/Info_Disclosure_CVE_2020_27986/poc.py``                    |
| SonicWall SSL-VPN         | SonicWall SSL-VPN 远程命令执行漏洞                                      | ``poc/SonicWall_SSL_VPN/RCE_jarrewrite/poc.py``                            |
| TamronOS IPTV系统           | TamronOS IPTV系统 后台配置敏感信息                                        | ``poc/TamronOS_IPTV/Info_Disclosure/poc.py``                               |
|                           | TamronOS IPTV系统存在前台命令执行漏洞                                       | ``poc/TamronOS_IPTV/RCE_api_ping/poc.py``                                  |
|                           | TamronOS IPTV系统 submit 任意用户创建漏洞                                 | ``poc/TamronOS_IPTV/User_Add_Submit/poc.py``                               |
| TCC_斗象                    | 斗象资产灯塔系统(ARL) 弱口令检测                                             | ``poc/TCC_斗象/Weak_Pass_ARL/poc.py``                                        |
|                           | Omnia MPX Node 不安全的直接对象引用(CVE-2022-43326)                       | ``poc/Telos_Alliance/IDOR_Omnia_MPX_Node_CVE_2022_43326/poc.py``           |
| ThinkPHP                  | ThinkPHP5 5.0.22/5.1.29 远程代码执行漏洞                                | ``poc/Thinkphp/RCE_5022_5129``                                             |
|                           | ThinkPHP5 5.0.23 远程代码执行漏洞                                       | ``poc/Thinkphp/RCE_5023/poc.py``                                           |
| 通达OA                      | 通达OA 计算机名探测插件                                                   | ``poc/Tongda_通达OA/Computer_Name_Plugin/poc.py``                            |
|                           | 通达OA 版本探测插件                                                     | ``poc/Tongda_通达OA/Version_Info_Plugin/poc.py``                             |
|                           | 通达OA2017 前台任意用户登录漏洞                                             | ``poc/Tongda_通达OA/AnyUser_Login_Version2017/poc.py``                       |
|                           | 通达OA v2017 video_file.php 任意文件下载漏洞                              | ``poc/Tongda_通达OA/FileRead_video_file/poc.py``                             |
|                           | 通达OA retrieve_pwd 任意用户登陆漏洞                                      | ``poc/Tongda_通达OA/AnyUser_Login_retrieve_pwd/poc.py``                      |
|                           | 通达OA < v11.7 auth_mobi.php 在线用户登录漏洞                             | ``poc/Tongda_通达OA/InfoDisclosure_auth_mobi/poc.py``                        |
|                           | 通达OA v11.9 getdata 任意命令执行漏洞                                     | ``poc/Tongda_通达OA/RCE_getdata/poc.py``                                     |
| 天融信                       | 天融信-上网行为管理系统 static_convert.php 命令注入漏洞                          | ``poc/TopSec_天融信/Common_Injection_static_convert/poc.py``                  |
| 同为股份                      | TVT数码科技 NVMS-1000 路径遍历漏洞                                        | ``poc/TVT_同为股份/Dir_Traversal_NVMS_1000/poc.py``                            |
| 艾泰科技                      | 艾泰网络管理系统弱口令                                                     | ``poc/UTT_艾泰科技/WeakPass_Net_Manager_System/poc.py``                        |
| 启明星辰                      | 天玥运维网关/网御网络审计 Sql注入漏洞                                           | ``poc/Venustech_启明星辰/SQLi_Reportguide/poc.py``                             |
| VMware                    | Vmware vCenter 任意文件读取                                           | ``poc/VMware/File_read_vCenter/poc.py``                                    |
|                           | VMware vRealize Operations Manager SSRF漏洞 CVE-2021-21975        | ``poc/VMware/SSRF_vRealize_CVE_2021_21975/poc.py``                         |
|                           | VMware Workspace ONE Access Freemarker 服务器端模板注入(CVE-2022-22954) | ``poc/VMware/CVE_2022_22954/poc.py``                                       |
|                           | VMware NSX Manager XStream 远程代码执行漏洞（CVE-2021-39144）             | ``poc/VMware/RCE_NSX_Manager_XStream_CVE_2021_39144/poc.py``               |
| VoIPmonitor               | VoIPmonitor 未授权远程代码执行(CVE-2021-30461)                           | ``poc/VoIPmonitor/RCE_CVE_2021_30461/poc.py``                              |
| WayOS 维盟                  | 维盟AC集中管理平台弱口令                                                   | ``poc/WayOS_维盟/WeakPass_AC_Manager/poc.py``                                |
| 泛微 OA                     | 泛微云桥 e-Bridge 任意文件读取漏洞                                          | ``poc/Weaver_泛微OA/File_Read_E_Bridge/poc.py``                              |
|                           | 泛微OA E-Office V9文件上传漏洞(CNVD-2021-49104)                         | ``poc/Weaver_泛微OA/File_Upload_E_Office_V9_CNVD_2021_49104/poc.py``         |
|                           | 泛微 e-cology OA 数据库配置信息泄露漏洞                                      | ``poc/Weaver_泛微OA/Config_Info_Disclosure_DBconfigReader/poc.py``           |
|                           | 泛微 OA 8 前台SQL注入                                                 | ``poc/Weaver_泛微OA/Sql_inj_E_cology_V8/poc.py``                             |
|                           | 泛微OA 日志泄露                                                       | ``poc/Weaver_泛微OA/Log_Disclosure/poc.py``                                  |
|                           | 泛微OA Beanshell 远程代码执行漏洞                                         | ``poc/Weaver_泛微OA/RCE_Beanshell/poc.py``                                   |
|                           | 泛微 E-cology WorkflowCenterTreeData.jsp文件 前台SQL注入漏洞              | ``poc/Weaver_泛微OA/Sql_Inj_E_cology_WorkflowCenterTreeData/poc.py``         |
|                           | 泛微V9 前台文件上传漏洞                                                   | ``poc/Weaver_泛微OA/File_Upload_V9_uploadOperation/poc.py``                  |
|                           | 泛微 E-cology V9信息泄露                                              | ``poc/Weaver_泛微OA/Config_Info_Disclosure_E_Cology_V9/poc.py``              |
|                           | 泛微 E-Office存在前台文件上传漏洞                                           | ``poc/Weaver_泛微OA/File_Upload_E_Office_ajax/poc.py``                       |
|                           | 泛微 E-office V9.5 SQL注入漏洞                                        | ``poc/Weaver_泛微OA/SQLi_E_Office_v9dot5/poc.py``                            |
|                           | 泛微OA E-Bridge saveYZJFile 任意文件读取漏洞                              | ``poc/Weaver_泛微OA/FileRead_saveYZJFile/poc.py``                            |
|                           | 泛微OA E-Office officeserver.php 任意文件读取漏洞                         | ``poc/Weaver_泛微OA/File_Read_E_Office_officeserver/poc.py``                 |
|                           | 泛微OA weaver.common.Ctrl 任意文件上传漏洞                                | ``poc/Weaver_泛微OA/File_Upload_weaver_common_ctrl/poc.py``                  |
|                           | 泛微e-cology登陆绕过                                                  | ``poc/Weaver_泛微OA/Login_Pass/poc.py``                                      |
|                           | 泛微云桥(e-bridge) addTaste存在sql注入漏洞                                | ``poc/Weaver_泛微OA/SQLi_E_Bridge_addTaste/poc.py``                          |
|                           | 泛微OA E-Office mysql_config.ini 数据库信息泄漏                          | ``poc/Weaver_泛微OA/InfoDisclosure_mysql_config_ini/poc.py``                 |
|                           | 泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞                        | ``poc/Weaver_泛微OA/FileRead_SignatureDownLoad/poc.py``                      |
| Weblogic                  | CVE-2016-0638                                                   | ``poc/Weblogic/CVE_2016_0638/poc.py``                                      |
|                           | Weblogic < 10.3.6 'wls-wsat' XMLDecoder 反序列化漏洞（CVE-2017-10271）  | ``poc/Weblogic/CVE_2017_10271/poc.py``                                     |
|                           | RCE_CVE-2018-3191                                               | ``poc/Weblogic/RCE_CVE_2018_3191/poc.py``                                  |
|                           | Weblogic SSRF (CVE-2014-4210)                                   | ``poc/Weblogic/SSRF_CVE_2014_4210/poc.py``                                 |
|                           | Weblogic 管理控制台未授权远程命令执行漏洞（CVE-2020-14882，CVE-2020-14883）        | ``poc/Weblogic/UnAuth_RCE_CVE_2020_14882/poc.py``                          |
|                           | Weblogic XMLDecoder反序列化漏洞（CVE-2017-3506）                        | ``poc/Weblogic/XMLDecoder_CVE_2017_3506/poc.py``                           |
| whir_万户软件                 | 万户ezoffice 前台sql注入                                              | ``poc/whir_万户软件/SQLi_EZOffice/poc.py``                                     |
|                           | 万户OA DownloadServlet 任意文件读取漏洞                                   | ``poc/whir_万户软件/FileDownload_DownloadServlet/poc.py``                      |
|                           | 万户OA downloadhttp.jsp 任意文件下载漏洞                                  | ``poc/whir_万户软件/FileDownload_downloadhttp_jsp/poc.py``                     |
|                           | 万户OA download_old.jsp 任意文件下载漏洞                                  | ``poc/whir_万户软件/FileDownload_download_old_jsp/poc.py``                     |
| 一米OA                      | 一米OA getfile.jsp 任意文件读取漏洞                                       | ``poc/YimiOA/ReadFile_getfile/poc.py``                                     |
| 用友NC                      | 用友NC6.5 BeanShell RCE                                           | ``poc/Yonyou_用友NC/RCE_BeanShell_CNVD_2021_30167/poc.py``                   |
|                           | 用友ERP-NC 目录遍历漏洞                                                 | ``poc/Yonyou_用友NC/Dir_List_ERP/poc.py``                                    |
|                           | 用友GRP-U8行政事业财务管理软件 SQL注入 CNNVD-201610-923                       | ``poc/Yonyou_用友NC/Sqli_CNNVD_201610_923/poc.py``                           |
|                           | 用友 时空KSOA 前台文件上传漏洞                                              | ``poc/Yonyou_用友NC/File_Upload_KSOA/poc.py``                                |
|                           | 用友 U8 OA test.jsp SQL注入漏洞                                       | ``poc/Yonyou_用友NC/SQLi_test_jsp/poc.py``                                   |
| Zabbix                    | Zabbix弱口令                                                       | ``poc/Zabbix/Weak_Pass/poc.py``                                            |
|                           | Zabbix SQL 注入漏洞(CVE-2016-10134)                                 | ``poc/Zabbix/SQLi_CVE_2016_10134/poc.py``                                  |
|                           | Zabbix未授权访问                                                     | ``poc/Zabbix/Auth_Bypass/poc.py``                                          |
| 禅道                        | 禅道8.2-9.2.1注入GetShell                                           | ``poc/Zentao_禅道/Getshell_test/poc.py``                                     |
| ZeroShell防火墙              | ZeroShell 3.9.0 远程命令执行漏洞                                        | ``poc/ZeroShell/RCE_kerbynet/poc.py``                                      |
| ZXOA_致翔OA                 | 致翔OA msglog.aspx SQL注入漏洞                                        | ``poc/ZXOA_致翔OA/SQLi_msglog_aspx/poc.py``                                  |
| Zyxel                     | Zyxel NBG2105身份验证绕过                                             | ``poc/Zyxel/Login_Pass_NBG2105/poc.py``                                    |
|                           | Zyxel 防火墙命令注入漏洞（CVE-2022-30525）                                 | ``poc/Zyxel/Command_Injection_CVE_2022_30525/poc.py``                      |

</details>
