const fs = require('fs/promises')

const zeroPad = (num, places) => String(num).padStart(places, '0')

const ZERO_PADDING = 4
const PASSWORDS_FILE_NAME = 'passwords.txt'

const main = async () => {
  await fs.truncate(PASSWORDS_FILE_NAME, 0)

  for (let i = 0; i <= 9999; i++) {
    await fs.appendFile(PASSWORDS_FILE_NAME, `${zeroPad(i, ZERO_PADDING)}\n`)
  }
}

main()
  .catch(console.error)
