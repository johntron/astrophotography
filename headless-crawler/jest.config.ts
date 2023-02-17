import type {Config} from 'jest';

const config: Config = {
    verbose: true,
    transform: {},
    testMatch: [ "**/__tests__/**/*.?(m)[jt]s?(x)", "**/?(*.)+(spec|test).?(m)[jt]s?(x)" ] // added support for .mjs
};

export default config;