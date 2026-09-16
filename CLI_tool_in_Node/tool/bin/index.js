#!/usr/bin/env node
import arg from 'arg'
import chalk from 'chalk'
import { pkgUp } from 'pkg-up';
import { createRequire } from 'node:module';
import start from '../src/commands/start.js';
import getConfig from '../src/config/config-mgr.js';
import createLogger from '../src/logger.js';
const logger = createLogger("bin")
const require = createRequire(import.meta.url);



try {
    const args = arg({
        '--start' : Boolean,
        '--build' : Boolean,
    })
    
    logger.debug("Recieved args" , args)
    if(args['--start']){

        const config = getConfig();
        start(config)
        // const pkgPath = pkgUp.sync({cwd: process.cwd()});
        // const pkg = require(pkgPath);
        // if (pkg.tool) {
        //     console.log('Found Configuration' , pkg.tool)
        // } else {
        //     console.log(chalk.yellow('Could not find Configuration using default'))
        // }
        // console.log(chalk.bgCyanBright("starting the app"))

    }
} catch (e) {
    logger.warning(e.message)
    // console.log(chalk.yellow(e.message));
    console.log()
    usage();
}

function usage(){
    console.log(`${chalk.whiteBright('tool [CMD]')}
        ${chalk.greenBright('--start\tStart the app')}
        ${chalk.greenBright('--build\tBuilds the app')}
        `);
}