#BioInfo_Project  
  
###Outline  
* [系統介面使用說明](#System_Interface)  
* [系統內容功能詳細敘述](#System_Content)  
* 建構本專案所使用的工具及版本  
	1. [Python **2.7.6**](#Python)  
	2. [Virtualenv **1.11.4**](#Virtualenv)  
	3. [Django **1.9**](#Django)  
* [專案執行教學](#Build_Step)  
* [工具安裝教學](#Tool_Install)  
* [Reference](#Reference)  
  
*************************************************************************************************************
  
<h3 id="System_Interface">系統介面使用說明</h3>  
![main page](https://raw.githubusercontent.com/Chienweichih/BioInfo_Project/master/snapshot/main.png)  
  
* **按下 Display All Data 按鈕，顯示所有可以 query 的 data**  
  
![display all](https://raw.githubusercontent.com/Chienweichih/BioInfo_Project/master/snapshot/display_all.png)  
  
* **在 Query Text: 後輸入要搜尋的詞，按下 query 按鈕就會顯示結果頁面**  
  
![query result](https://raw.githubusercontent.com/Chienweichih/BioInfo_Project/master/snapshot/query.png)  
  
* **在 Abstract Text: 後輸入要處理的論文摘要，按下 analysis 按鈕就會顯示結果頁面**  
  
![abstract result](https://raw.githubusercontent.com/Chienweichih/BioInfo_Project/master/snapshot/abstract.png)  
  
*************************************************************************************************************
  
<h3 id="System_Content">專案內容功能詳細敘述</h3>  
這個 Python 檔案紀錄系統載入頁面時需要做的所有動作:  
  
	> BioInfo_Project/bioPortal/views.py  
  
這個專案所顯示的 html 介面的 template 放在這個資料夾下：  
  
	> BioInfo_Project/bioPortal/templates/bioPortal/  
  
html 用到的 form 寫在這裡：  
  
	> BioInfo_Project/bioPortal/forms.py  
  
系統要處理的 url request 寫在這裡：  
  
	> BioInfo_Project/bioPortal/urls.py  
  
這兩個檔案是 bioPortal 的 [Gene Ontology](https://bioportal.bioontology.org/ontologies/GO)，在程式執行時要讀取的檔案：  
  
	> BioInfo_Project/go_name.data  
	> BioInfo_Project/go_term.data  
  
其他的就是 Django 專案需要的程式，如果想要了解可以閱讀 Django 的相關文件  
  
*************************************************************************************************************
  
<h3 id="Build_Step">專案執行教學</h3>  
如果已經安裝  
	1. [Python **2.7.6**](#Python)  
	2. [Virtualenv **1.11.4**](#Virtualenv)  
	3. [Django **1.9**](#Django)  
可以直接執行：  
  
打開 *終端機* 或 *命令提示字元* ，移動目錄到 BioInfo_Project 資料夾內  
  
執行  
  
	> python manage.py runserver 0.0.0.0:8000  
  
打開瀏覽器，網址輸入  
  
	> http://localhost:8000/  
  
就可以看到網站頁面  
  
*************************************************************************************************************
  
<h3 id="Tool_Install">工具安裝教學</h3>  
* <h4 id="Python">Python</h4>  
	* Windows 或 OS X 系統：  
	從[Pyhton官網](https://www.python.org/)下載第二版的Python安裝檔，依照提示步驟安裝即可 （記得安裝的路徑）  
	  
	* Debian/Ubuntu 系統：  
	在終端機輸入以下指令：  
		  
		> sudo apt-get install python  
	  
	* Red Hat/Fedora 系統：  
		  
		> sudo yum install python  
  
* <h4 id="Virtualenv">Virtualenv</h4>  
	在開發 Python 專案的時候，通常會使用 virtualenv。使用 virtualenv 的好處如下：  
	1. 每一個專案可以創造出獨立的環境。如此就不會因為其他專案的 Library 升級而導致專案出問題。  
	2. 當專案需要移到其他機器上頭的時候，相依的套件比較好處理  
  
	**Ubuntu 系統安裝**  
	  
	> sudo apt-get install python-virtualenv  
	  
	  
	**其他-使用 pip 安裝**  
	  
	先確認系統有沒有安裝 pip。直接輸入以下指令：  
	  
	> pip  
	  
	如果看到以下內容：  
  
		Usage:  
		pip <command> [options]  
		  
		Commands:  
		install                     Install packages.  
		uninstall                   Uninstall packages.  
		[以下略…]  
  
	就代表已經有 pip 了，直接開始安裝 virtualenv。  
  
	*安裝 pip:*  
  
	下載 [get-pip.py](https://bootstrap.pypa.io/get-pip.py) 這個檔案。切換至該檔案的目錄，用 Python 執行它：  
  
	> python get-pip.py  
  
	即可完成安裝。完成後請再次試著執行 pip 指令，以確認安裝是否成功。  
	  
	**安裝 Virtualenv**  
	  
	> pip install virtualenv  
  
	(可能會需要管理員權限)  
  	
	<h4 id="Virtualenv">建立 Virtualenv 環境</h4>  
	安裝好之後，就可以建立 virtualenv 環境，在 terminal 底下輸入：  
  	
	> virtualenv env  
  
	（若要指定 virtualenv 使用的 Python 版本，輸入：）  
  
	> virtualenv -p /usr/bin/python2.6 env  
  
	接下來輸入  
  
	> source env/bin/activate  
  
	（Windows 系統輸入）  
  
	> env\Scripts\activate  
  
	就可以啟動 virtualenv，從此只要在 virtualenv 下面安裝的 package 都只會存在於這個 virtualenv 當中。  
  
	<h4>結束 Virtualenv 環境</h4>  
  
	輸入  
  
	> deactivate  
  
	就可以結束 Virtualenv 環境  
  
* <h4 id="Django">Django</h4>  
  
	在 terminal 底下輸入：  
  
	> pip install django  
  
	便會下載最新版的 django 並且完成安裝。  
  
*************************************************************************************************************
  
<h3 id="Reference">Reference</h3>  
  
此 project 所用的資料庫是 BioPortal  
http://bioportal.bioontology.org/  
  
使用這個 Gene Ontology  
https://bioportal.bioontology.org/ontologies/GO  
  
Django 的教學  
https://daikeren.gitbooks.io/django_tutorial/content/django/README.html  
https://docs.djangoproject.com/en/1.9/  
  
其他：  
  
ncbo sample code  
https://github.com/ncbo/ncbo_rest_sample_code  
https://github.com/ncbo/bioportal-sparql-proxy  
  
BioPortal 的 api，用REST跟他要資料  
https://www.biocatalogue.org/services/2053  
  
Django REST的使用  
http://www.django-rest-framework.org/  
  
Secure tunnels to localhost  
https://ngrok.com/  
  
將 markdown 檔轉成 html 以便輸出  
https://github.com/joeyespo/grip  

