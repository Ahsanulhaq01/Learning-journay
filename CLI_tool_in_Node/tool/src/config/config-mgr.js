import chalk from "chalk";
import { cwd } from "node:process";
import schema from './schema.json' with {type : 'json'}
import {cosmiconfigSync} from 'cosmiconfig'
import Ajv from 'ajv'
import betterAjvErrors from 'better-ajv-errors'
const configLoader = cosmiconfigSync("tool")
import { createRequire } from "node:module";
const require = createRequire(import.meta.url)
const pkgUP = require("pkg-up")

const ajv = new Ajv({ jsonPointers : 'true' });

function getConfig() {
    const result = configLoader.search(process.cwd());
    if (!result) {
    console.log(chalk.yellow('Could not find configuration, using default'));
    return { port: 1234 };
  } else {
    const isValid = ajv.validate(schema , result.config)
    if(!isValid){
      console.log(chalk.yellow("Invalid Configuration was supplied"))
      console.log()

      console.log(betterAjvErrors(schema , result.config ,ajv.errors))
      
      process.exit(1);
    }

    console.log('Found configuration', result.config);
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