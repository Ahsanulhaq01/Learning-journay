import chalk from "chalk";
import { cwd } from "node:process";
import {cosmiconfigSync} from 'cosmiconfig'
const configLoader = cosmiconfigSync("tool")
import { createRequire } from "node:module";
const require = createRequire(import.meta.url)
const pkgUP = require("pkg-up")

function getConfig() {
    const result = configLoader.search(process.cwd());
    if (!result) {
    console.log(chalk.yellow('Could not find configuration, using default'));
    return { port: 1234 };
  } else {
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