from pyobigram.utils import sizeof_fmt
from pyobigram.utils import sizeof_fmt,get_file_size,createID
from pyobigram.client import ObigramClient,inlineQueryResultArticle
from MoodleClient import MoodleClient

from JDatabase import JsonDatabase
import zipfile
import os
import infos
import xdlink
import mediafire
from megacli.mega import Mega
import megacli.megafolder as megaf
import megacli.mega
import datetime
import time
import youtube
import NexCloudClient

from pydownloader.downloader import Downloader
from ProxyCloud import ProxyCloud
import ProxyCloud
import socket
import tlmedia
import S5Crypto

def createDownloading(filename,totalBits,currentBits,speed,tid=''):
    msg = '📥Descargando... \n'
    msg+= '🔖Nombre: ' + str(filename)+'\n'
    msg+= f'🗂Tamaño: {str(sizeof_fmt(currentBits))} - {str(sizeof_fmt(totalBits))}\n'
    msg+= f'📶Velocidad: {str(sizeof_fmt(speed))}/s\n\n'
    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,originalname=''):
    msg = '⏫Subiendo A La Nube☁... \n\n'
    msg+= '🔖Nombre: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '⏫Subiendo: ' + str(filename)+'\n'
    msg+= f'🗂Tamaño: {str(sizeof_fmt(currentBits))} - {str(sizeof_fmt(totalBits))}\n'
    msg+= f'📶Velocidad: {str(sizeof_fmt(speed))}/s\n\n'
    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '📚Comprimiendo... \n\n'
    msg+= '🔖Nombre: ' + str(filename)+'\n'
    msg+= '🗂Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📂Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '💾Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '📌Proceso Finalizado📌\n\n'
    msg+= '🔖Nombre: ' + str(filename)+'\n'
    msg+= '🗂Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📂Tamaño Partes: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= '📤Partes Subidas: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '🗑Borrar Archivo: ' + '/borrar_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>《Enlaces》</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = f'《Archivos》 {str(len(evfiles))}📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                #fname = f['name'] + fext
                fname = f['name']
                msg+= '<b>------------------------------------------</b>\n'
                msg+= '<b>📄'+ fname +'</b>\n'
                msg+= '🗑<b>/borrar_'+str(i)+'</b>\n'
                msg+= '📝<b>/txt_'+str(i)+'</b>\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '⚙️Configuraciones⚙️\n\n'
    msg+= '》Nombre: @' + str(username)+'\n'
    msg+= '》Usuario: ' + str(userdata['moodle_user'])+'\n'
    msg+= '》Contraseña: ' + str(userdata['moodle_password'])+'\n'
    msg+= '》Pagina: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '》RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
        if userdata['uploadtype'] == 'evidence':
            msg+= '》Lugar: Evicencias\n'
            pass
        if userdata['uploadtype'] == 'draft':
            msg+= '》Lugar: Privados\n'
            pass
        if userdata['uploadtype'] == 'blog':
            msg+= '》Lugar: Blogs\n'
            pass
        #msg+= '》Lugar: ' + str(userdata['uploadtype'])+'\n'

    msg+= '》CloudType: ' + str(userdata['cloudtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '》Dir: /' + str(userdata['dir'])+'\n'
    msg+= '》Tamaño: ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = '❌'
    if isadmin:
        msgAdmin = '✅'
    msg+= '》Admin : ' + msgAdmin + '\n'
    proxy = '❌'
    if userdata['proxy'] !='':
       proxy = '✅'
    msg+= '》Proxy : ' + proxy + '\n\n'
    return msg

def createnew(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = 'Noticias\n\n'
    msg+= 'Hola @' + str(username)+'\n'
    new = open('new.txt','r')
    bot.sendMessage(update.message.chat.id,new.read())
    new.close()
    return msg
bot_token = os.environ.get('bot_token')
    #set in debug
    bot_token = '5151452599:AAEv-wbg_V8m1Ep-8Q3R5vsmh4sDY1lUmiI'

    bot = ObigramClient(bot_token)
    bot.onMessage(onmessage)
    bot.run()

if __name__ == '__main__':
    try:
        main()
    except:
        main()
