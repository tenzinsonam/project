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
        let tesy = new String
        /*
        fs.readFile('temp.c','r',function(err, data){
            tesy = data
        })
        */
        fs.readFile('wolo.txt',function(err, data){
            //console.log('hello')
            tesy = data.toString('utf-8')
            //console.log(data.toString('utf-8'))
        })
        let position = editor.selection.active
        let terminal = vscode.window.createTerminal()
        //terminal.show()
        //terminal.sendText('cd /home/tenzin/Downloads/asdf')
        //terminal.sendText('python test.py')
        terminal.sendText('pwd')
        let decs = []
        let l = position.line + 1
        let c = position.character + 1
        let pos = new vscode.Position(l,c)        //let pos
        //await
        //pos.line = position.line + 1
        //pos.character = position.character + 1
        let decorationType = vscode.window.createTextEditorDecorationType({
            backgroundColor: 'red'
            //borderWidth: '2px',
            //borderStyle: 'solid'
        })
        let pos1 = new vscode.Range(1,1,1,7)
        let pos2 = new vscode.Range(0,1,0,8)
        decs.push(pos1)
        decs.push(pos2)
        function delay(ms: number){
            return new Promise(resolve => setTimeout(resolve, ms))
        }

        //await delay(3000)
        setTimeout(function(){
            console.log('adas')
        },3000)
        
        editor.setDecorations(decorationType,decs)
        //vscode.commands.executeCommand('workbench.action.tasks.runTask')
        //var spawn = require("child_process").spawn
        //var process = spawn('python',["/home/tenzin/Downloads/asdf/test.py"])
        
        console.log(tesy)
    });

    context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
export function deactivate() {
}