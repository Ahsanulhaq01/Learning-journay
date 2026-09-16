import chalk from "chalk";
import { cwd } from "node:process";
import schema from './schema.json' with {type : 'json'}
import {cosmiconfigSync} from 'cosmiconfig'
import Ajv from 'ajv'
import betterAjvErrors from 'better-ajv-errors'
import createLogger from "../logger.js";
const logger = createLogger('config:mgr')
const configLoader = cosmiconfigSync("tool")
import { createRequire } from "node:module";
const require = createRequire(import.meta.url)
const pkgUP = require("pkg-up")

const ajv = new Ajv({ jsonPointers : 'true' });

function getConfig() {
    const result = configLoader.search(process.cwd());
    if (!result) {
      logger.warning("could not find configuration , using default")
    // console.log(chalk.yellow('Could not find configuration, using default'));
    return { port: 1234 };
  } else {
    const isValid = ajv.validate(schema , result.config)
    if(!isValid){
      logger.warning("Invalid configuration was Supplied")
      // console.log(chalk.yellow("Invalid Configuration was supplied"))
      console.log()

      console.log(betterAjvErrors(schema , result.config ,ajv.errors))
      
      process.exit(1);
    }
    logger.debug("found configurtion" , result.config)
    // console.log('Found configuration', result.config);
    return result.config;
  }
    // const pkgPath = pkgUp.sync({ cwd: process.cwd() })
    // const pkg = require(pkgPath)

    // if (pkg.tool) {
    //     console.log("Found Configuration", pkg.tool);
    //     return pkg.tool
    // } else if (hasJSConfigFile()) {
    //     return loadJSConfigFile();
    // }
    // else {
    //     console.log(chalk.yellow("Could not find Configuration using default"))
    //     return { port: 1234 }
    // }

}

export default getConfig;