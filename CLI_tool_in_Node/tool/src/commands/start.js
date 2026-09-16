import chalk from 'chalk'
import createLogger from '../logger.js'
const logger = createLogger('commands:start')

function start(config){
    logger.highlight("Starting the app");
    logger.debug("Recieved Configuration" , config)
}


export default start