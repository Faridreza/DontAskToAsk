from email import message
import pyrogram as Bot
import requests

GroupQuestion = Bot.Client("GroupQuestion", api-id,api-hash)


ListQuestion = [
    "میتونم",
    "می تونم",
    "می تونه",
    "میتونه",
    "بلده",
    "یاد داره",
    "دارم",
    "کسی اینجا",
    "داره",
    "سوال",
    "چطور",
    "اینجا",
    "کرده",
    "چطوری",
    "چیه",
    "مشکل",
    "مشکلی",
    "میخام",
    "می خام",
    "می خوام",
    "میخوام",
    "کسی",
    "چرا",
    "کار نمیکنه",
    "کار نمی کنه",
    "نمیکنه",
    "نمی کنه",
    "میتونین",
    "می تونی",
    "میتونی",
    "می تونین"
]


MessageSugest="سلام دوسته خوبم❤️\n\nی پیشنهاد برات دارم برای پیشرفت خودت و برای سوالی که پرسیدی🌹\n\nبهت پیشنهاد میکنم وقتی سوالی برات پیش میاد اول داخل گوگل،یوتیوب یا هرجای دیگه سرچ کنی تا هم مهارت سرچ کردنت بره بالا هم به جواب درستی برسی👌\n\nقطعا سوالی که الان واست پیش اومده قبلا برای یکی دیگه هم پیش اومده پس داخل اینترنت بهتر و سریع تر به جوابت میرسی پس اول سرچ کن بعد بیا گروه بپرس تا به نتیجه بهتری برسی🌹\n\nحالا اگه میخای من برات چیزیو سرچ کنم و حال نداری بری گوگل رو پیامم ریپلای کن و سوالت رو اینطوری طرح کن\n\n\nجمع دو عدد در سی شارپ\n\nمن واست لینک مستقیم گوگل رو میارم :)❤️"

@GroupQuestion.on_message(Bot.filters.group)
async def GroupQuestionMessage(_: GroupQuestion, e: Bot.types.Message):
    try:
        if e.chat.id==##User ID Group##:
            UserIsBot=e.from_user.is_bot
            UserId=e.from_user.id
            if UserIsBot==False:
              MessageId=e.message_id
              if e.text != None:
                    MessageText=e.text
                    if MessageText==MessageSugest and UserId != ##User ID Admin Self##:
                        await GroupQuestion.delete_messages(##User ID Group##,MessageId)
                    elif e.reply_to_message!=None and e.reply_to_message.text==MessageSugest:
                        Result="رو لینک کلیک کن تا به جواب سوالت برسی❤️\nسرچ کردن کار سختی نیست یادش بگیر :) \n\n\n=> <a href=http://bmbgk.ir/?q={txt}>{message}</a> <=".format(txt=MessageText.replace(" ","+"),message=MessageText)
                        await GroupQuestion.send_message(##User ID Group##,Result,reply_to_message_id=MessageId)
                    else:
                        for Q in ListQuestion:
                            if MessageText.__contains__(Q):
                                 await GroupQuestion.send_message(##User ID Group##,MessageSugest,reply_to_message_id=MessageId)
                                 break       
              elif e.media=="photo" or e.document.mime_type=="image/jpeg":
                    Caption=e.caption
                    for Q in ListQuestion:
                        if Caption.__contains__(Q):
                             await GroupQuestion.send_message(##User ID Group##,MessageSugest,reply_to_message_id=MessageId)
                             break
    except:
        pass
        

GroupQuestion.run()