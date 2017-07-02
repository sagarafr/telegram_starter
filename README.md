# Read me

## Build status

[![Build Status](https://travis-ci.org/sagarafr/telegram_starter.svg?branch=master)](https://travis-ci.org/sagarafr/telegram_starter)

## Introduction

A basic starter for python-telegram-bot.

## How to add command
Just create all needed command in the directory commands. To signal a function as a command
just use the decorator @Command. Look cmd_help.py or cmd_start.py files for more examples.

## How to add token
To add the token given by the BotFather, just put in the file configuration.ini in resources
directory.
