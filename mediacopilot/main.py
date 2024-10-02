import logging
import os
from dotenv import load_dotenv
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)
import keyboard, text_for_mess, back


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='app.log', 
    filemode='w'
)

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('admin_id')
lst_users = []
lst_question = []
flag_oper = True


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    kb = InlineKeyboardMarkup(keyboard.kb_start)
    await update.message.reply_text("Выберите интересующую вас тему:", reply_markup=kb)

async def start_call(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_start)
    await query.edit_message_text("Выберите интересующую вас тему:", reply_markup=kb)
###start callbacks
async def info(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_info)
    await query.edit_message_text(text=text_for_mess.text_info, reply_markup=kb)


async def student(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    kb = InlineKeyboardMarkup(keyboard.kb_student)
    await query.edit_message_text(text=text_for_mess.text_student, reply_markup=kb)

async def activities(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    kb = InlineKeyboardMarkup(keyboard.kb_activities)
    await query.edit_message_text(text=text_for_mess.text_activities, reply_markup=kb)


async def study(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_study)
    await query.edit_message_text(text=text_for_mess.text_study, reply_markup=kb)

async def army(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_stud)
    await query.edit_message_text(text=text_for_mess.text_army, reply_markup=kb)

async def home(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_stud)
    await query.edit_message_text(text=text_for_mess.text_home, reply_markup=kb)

async def contact(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_contact)
    await query.edit_message_text(text=text_for_mess.text_contact, reply_markup=kb)

async def SA(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_SA)
    await query.edit_message_text(text=text_for_mess.text_SA, reply_markup=kb)

async def media(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_media)
    await query.edit_message_text(text=text_for_mess.text_media, reply_markup=kb)

async def another(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another)
    await query.edit_message_text(text=text_for_mess.text_activities_another, reply_markup=kb)


async def korpus(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_ycheb)
    await query.edit_message_text(text=text_for_mess.text_korpus, reply_markup=kb)

async def map(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_ycheb)
    await query.edit_message_text(text=text_for_mess.text_map, reply_markup=kb)

async def it(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_korp_contact)
    await query.edit_message_text(text=text_for_mess.text_it, reply_markup=kb)

async def gum(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_korp_contact)
    await query.edit_message_text(text=text_for_mess.text_gum, reply_markup=kb)

async def psit(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_korp_contact)
    await query.edit_message_text(text=text_for_mess.text_psit, reply_markup=kb)

async def SNO(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_SA_activ)
    await query.edit_message_text(text=text_for_mess.text_SA_SNO, reply_markup=kb)

async def cultorg(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_SA_activ)
    await query.edit_message_text(text=text_for_mess.text_SA_cultorg, reply_markup=kb)

async def sportorg(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_SA_activ)
    await query.edit_message_text(text=text_for_mess.text_SA_sportorg, reply_markup=kb)

#########################################################
async def volonter(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_volonter, reply_markup=kb)

async def VIAR(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_VIAR, reply_markup=kb)

async def finans(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_finans, reply_markup=kb)

async def games(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_games, reply_markup=kb)

async def mathchess(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_mathchess, reply_markup=kb)

async def theatre(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_theatre, reply_markup=kb)

async def sport(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_sport, reply_markup=kb)

async def bisness(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_bisness, reply_markup=kb)

async def struna(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_struna, reply_markup=kb)

async def druzina(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_druzina, reply_markup=kb)

async def strelok(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_strelok, reply_markup=kb)

async def reconstruct(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_reconstruct, reply_markup=kb)

async def turism(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_turism, reply_markup=kb)

async def historyclub(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_historyclub, reply_markup=kb)

async def pravo(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_pravo, reply_markup=kb)

async def hotel(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_another_activ)
    await query.edit_message_text(text=text_for_mess.text_another_hotel, reply_markup=kb)

async def correct_answer(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Спасибо за отзыв")
    lst_question.remove(context.user_data['user_question'])
    lst_users.remove(context.user_data['user_id'])

async def uncorrect_answer(update: Update, context):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(text="Спасибо за отзыв, мы перенаправили ваш вопрос оператору, ожидайте ответа")
    if len(lst_question) == 1:
        await context.bot.send_message(chat_id=admin_id, text=f"Вопрос от пользователя: {lst_question[0]}")


###end callbacks
async def feedback(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_feedback)
    await query.edit_message_text(text=text_for_mess.text_feedback, reply_markup=kb)

async def get_message(update: Update, context):
    user_id = update.effective_user.id
    context.user_data['user_id'] = user_id

    if user_id != admin_id:
        if user_id not in lst_users:
            lst_users.append(user_id)
            user_message = update.message.text
            context.uesr_data['user_question'] = user_message
            lst_question.append(user_message)
            answer = back.get_info(user_message)

            if answer == []:
                await context.bot.send_message(chat_id=user_id, text="Мы перенаправили ваш вопрос оператору, ожидайте ответа")
                if len(lst_question) == 1:
                    await context.bot.send_message(chat_id=admin_id, text=f"Вопрос от пользователя: {user_message}")
            else:
                kb = InlineKeyboardMarkup(keyboard.kb_answer)
                await update.message.reply_text(text=answer[0][0], reply_markup=kb)

        else:
            await context.bot.send_message(chat_id=user_id, text=f"Вы уже задали вопрос, дождитесь пока оператор ответит на ваш предыдущий вопрос, а затем задавайте следующий.")
    else:
        answer = update.message.text

        kb = InlineKeyboardMarkup(keyboard.kb_oper)
        update.message.reply_text(text="Вы ответили на вопрос пользователя, хотите продолжить?", reply_markup=kb)

        await context.bot.send_message(chat_id=lst_users[0], text=f"Ответ от оператора: {answer}")
        lst_users.pop(0)
        lst_question.pop(0)

async def operator(update: Update, context):
    query = update.callback_query
    await query.answer()

    if lst_question:
        await context.bot.send_message(chat_id=admin_id, text=f"Вопрос от пользователя: {lst_question[0]}")
    else:
        await context.bot.send_message(chat_id=admin_id, text=f"Больше вопросов нету.")

async def stop_question(update: Update, context):
    query = update.callback_query
    await query.answer()

    kb = InlineKeyboardMarkup(keyboard.kb_stop_question)
    await query.edit_message_text(text=text_for_mess.text_stop_question, reply_markup=kb)


def main() -> None:
    application = Application.builder().token(token).build()


    application.add_handler(CallbackQueryHandler(feedback, "start_question"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_message))
    application.add_handler(CallbackQueryHandler(stop_question, "question_stop"))
    application.add_handler(CallbackQueryHandler(correct_answer, "answer_correct"))
    application.add_handler(CallbackQueryHandler(uncorrect_answer, "answer_uncorrect"))
    application.add_handler(CallbackQueryHandler(operator, "next_question"))


    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(start_call, "start_call"))
    
    application.add_handler(CallbackQueryHandler(info, "start_info"))

    application.add_handler(CallbackQueryHandler(activities, "info_activities"))
    application.add_handler(CallbackQueryHandler(student, "info_student"))

    application.add_handler(CallbackQueryHandler(study, "student_study"))
    application.add_handler(CallbackQueryHandler(army, "student_army"))
    application.add_handler(CallbackQueryHandler(home, "student_home"))
    application.add_handler(CallbackQueryHandler(contact, "student_contact"))
    #######################################################################
    application.add_handler(CallbackQueryHandler(SA, "activities_SA"))
    application.add_handler(CallbackQueryHandler(media, "activities_media"))
    application.add_handler(CallbackQueryHandler(another, "activities_another"))

    application.add_handler(CallbackQueryHandler(korpus, "study_korpus"))
    application.add_handler(CallbackQueryHandler(map, "study_map"))
    application.add_handler(CallbackQueryHandler(it, "contact_it"))
    application.add_handler(CallbackQueryHandler(gum, "contact_gum"))
    application.add_handler(CallbackQueryHandler(psit, "contact_psit"))
    #######################################################################
    application.add_handler(CallbackQueryHandler(SNO, "SA_SNO"))
    application.add_handler(CallbackQueryHandler(cultorg, "SA_cultorg"))
    application.add_handler(CallbackQueryHandler(sportorg, "SA_sportorg"))

    application.add_handler(CallbackQueryHandler(volonter, "another_volonter"))
    application.add_handler(CallbackQueryHandler(VIAR, "another_VIAR"))
    application.add_handler(CallbackQueryHandler(finans, "another_finans"))
    application.add_handler(CallbackQueryHandler(games, "another_games"))
    application.add_handler(CallbackQueryHandler(mathchess, "another_mathchess"))
    application.add_handler(CallbackQueryHandler(theatre, "another_theatre"))
    application.add_handler(CallbackQueryHandler(sport, "another_sport"))
    application.add_handler(CallbackQueryHandler(bisness, "another_bisness"))
    application.add_handler(CallbackQueryHandler(struna, "another_struna"))
    application.add_handler(CallbackQueryHandler(druzina, "another_druzina"))
    application.add_handler(CallbackQueryHandler(strelok, "another_strelok"))
    application.add_handler(CallbackQueryHandler(reconstruct, "another_reconstruct"))
    application.add_handler(CallbackQueryHandler(turism, "another_turism"))
    application.add_handler(CallbackQueryHandler(historyclub, "another_historyclub"))
    application.add_handler(CallbackQueryHandler(pravo, "another_pravo"))
    application.add_handler(CallbackQueryHandler(hotel, "another_hotel"))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()