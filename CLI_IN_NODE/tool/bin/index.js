#!/usr/bin/env node
import arg from 'arg'
import chalk from 'chalk'
import pkg from './../../testProject/package.json';
try {
    const args = arg({
        '--start' : Boolean,
        '--build' : Boolean,
    })
    
    if(args['--start']){
        
        console.log(chalk.bgCyanBright("starting the app"))

    }
} catch (e) {
    console.log(chalk.yellow(e.message));
    console.log()
    usage();
}

function usage(){
    console.log(`${chalk.whiteBright('tool [CMD]')}
        ${chalk.greenBright('--start\tStart the app')}
        ${chalk.greenBright('--build\tBuilds the app')}
        `);
}