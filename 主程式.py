from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackContext

# 初始化機器人
API_TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN"  # 替換為你的 API token

# 定義處理指令的函數
async def delete_command(update: Update, context: CallbackContext) -> None:
    # 確認訊息是指令
    if update.message.text.startswith('/'):
        # 獲取當前聊天的管理員列表
        chat_admins = await context.bot.get_chat_administrators(update.message.chat_id)
        admin_ids = [admin.user.id for admin in chat_admins]

        # 檢查訊息是否由機器人自己或管理員發送
        if update.message.from_user.id != context.bot.id and update.message.from_user.id not in admin_ids:
            # 刪除訊息
            await update.message.delete()

# 初始化 Telegram 機器人應用
def main():
    application = ApplicationBuilder().token(API_TOKEN).build()

    # 添加過濾器來處理所有的指令訊息
    application.add_handler(MessageHandler(filters.COMMAND, delete_command))

    # 啟動機器人
    application.run_polling()

if __name__ == '__main__':
    main()
