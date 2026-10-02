const mineflayer = require('mineflayer')

const bot = mineflayer.createBot({
  host: 'llama.aternos.host', 
  port: 31511,
  username: 'PoorOsuPlayer'
})

bot.once('spawn', () => {
  bot.chat(`/skin set V3lly_`)
  bot.chat(`/msg Korista_ Привет, я защитная установка "${bot.username}". Пожалуйста прими мой tpa запрос на нужном тебе месте!`)
})

bot.on('chat', (username, message) => {
  if (username === bot.username) return
  if (message === 'hi') bot.chat(`Hi ${username}!`)
})

bot.on('kicked', console.log)
bot.on('error', console.log)