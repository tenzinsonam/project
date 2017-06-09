'use strict';
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {



    console.log('Congratulations, your extension "rep" is now active!');

    // The command has been defined in the package.json file
    // Now provide the implementation of the command with  registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
    let editor = vscode.window.activeTextEditor
    let position = editor.selection.active
    let terminal = vscode.window.createTerminal()
    let correctPos = new vscode.Position(position.line+1,position.character+1)
    //let stri = 'in.py ' + String(correctPos.line)+ ' ' + String(correctPos.character)
    //console.log(stri)
    //terminal.show()
    //terminal.sendText(stri)
    var PythonShell = require('python-shell')
    var options = {
        args: [String(correctPos.line),String(correctPos.character)]
    }
    PythonShell.run('in.py', options, function(err, data){
        //console.log('hello')
        if (err) throw err
        let arr = []
        let i =0
        while(data[i]!=''){
            arr.push(data[i])
            i++
        }
        let dan = arr.pop()
        let ran = dan.split(',')
        arr.push('')
        i=0
        console.log(ran)
        let stri = ''
        while(arr[i]!=''){
            stri += arr[i] + '\n'
            i++
        }
        stri = stri.slice(0,-1)
        let np = new vscode.Position(Number(ran[0])-1,Number(ran[1])-1)
        let p2 = new vscode.Position(Number(ran[2])-1,Number(ran[3])-1)
        let r1 = new vscode.Range(np,p2)
        //console.log(Number(ran[2])-1)
        //console.log(np)
        //console.log(r1)
        editor.edit(function(editBuilder){
            editBuilder.delete(r1)
            editBuilder.insert(np, stri)
            
        })
        //console.log(ran)
        //console.log(arr)
    })
    
   
    });

    context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
export function deactivate() {
}