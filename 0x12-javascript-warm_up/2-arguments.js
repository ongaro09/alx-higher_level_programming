#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length === 2) {
  console.log('No arguments');
} else {
  console.log('Argument found');
}
