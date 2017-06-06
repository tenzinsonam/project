'use strict';
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as fs from 'fs';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

    // Use the console to output diagnostic information (console.log) and errors (console.error)
    // This line of code will only be executed once when your extension is activated
    console.log('Congratulations, your extension "asdf" is now active!');

    // The command has been defined in the package.json file
    // Now provide the implementation of the command with  registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        let editor = vscode.window.activeTextEditor
        let text = editor.document.getText()
         let decorationType = vscode.window.createTextEditorDecorationType({
            backgroundColor: 'red'
            //borderWidth: '2px',
            //borderStyle: 'solid'
        })
        var PythonShell = require('python-shell');
        PythonShell.run('test.py', function (err) {
            if (err) throw err;
            var lineReader = require('readline').createInterface({
                input: require('fs').createReadStream('nibba.txt')
            });

            let i = 1;
            let decs = []  
            lineReader.on('line', function (line) {
                if(i%4==0){
                    let line_split = line.split(",");
                    console.log('Line from file:', line_split);     
                    let pos1 = new vscode.Range(parseInt(line_split[0]),parseInt(line_split[1]),parseInt(line_split[2]),parseInt(line_split[3]));
                    //console.log(pos1);
                    decs.push(pos1);      
                    editor.setDecorations(decorationType,decs);
                }
                i+=1;
            });
        });
        
        let position = editor.selection.active
        let terminal = vscode.window.createTerminal()

    });

    context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
export function deactivate() {
}