import #Primero se debe instalar:
pip install python-telegram-bot

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    
    update.message.reply_text('Bienvenido estimado comensal!')
    update.message.reply_text('Este es el prototipo de un chat bot para cafeterias')
    update.message.reply_text('Puede ver nuestras opciones presionando /ayuda')

def ayuda(update, context):
    
    update.message.reply_text('Puede consultar la comida presionando /comida')
    update.message.reply_text('Puede consultar las bebidas presionando /bebida')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def comida(update, context):
    update.message.reply_text("El menu de hoy es: ")
    update.message.reply_text("Sopa fria, huevo a la mexicana con frijoles y totopos, postre y agua de limon ")
    update.message.reply_text("A tan solo $40")
    update.message.reply_text("En seguida llegara un empleado para tomar su orden si desea revisar las bebidas presione /bebida")



def bebida(update, context):
    update.message.reply_text("Contamos con las siguientes bebidas: ")
    update.message.reply_text("Michelada        $60")
    update.message.reply_text("Jarra de agua    $30")
    update.message.reply_text("CoCaCola         $20")
    update.message.reply_text("Pepsi            $15")
    update.message.reply_text("En seguida llegara un empleado para tomar su orden")



def main():
    updater = Updater("1005504972:AAFm3Q0cgKH4Esh422ZREmk7pNOeDDPMZfk", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ayuda", ayuda))
    dp.add_handler(CommandHandler("comida", comida))
    dp.add_handler(CommandHandler("bebida", bebida))
    

    
    dp.add_error_handler(error)

    updater.start_polling()
   
    updater.idle()
if __name__ == '__main__':
    main()
