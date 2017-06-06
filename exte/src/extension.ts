'use strict';
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import { commands, ExtensionContext, window, OverviewRulerLane, workspace, Range, QuickPickItem } from 'vscode';


// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: ExtensionContext) {
    

    
    //let word = 'strcpy' ;                      //keep same
    let regEx = /strcpy\(\w+\,\w+\)/g
    // Use the console to output diagnostic information (console.log) and errors (console.error)
    // This line of code will only be executed once when your extension is activated
    console.log('Congratulations, your extension "zest" is now active!');

    // The command has been defined in the package.json file
    // Now provide the implementation of the command with  registerCommand
    // The commandId parameter must match the command field in package.json
    commands.registerCommand('dontsayHello', () => {
        
                        updateDecorations();
        
    })

    commands.registerCommand('sayHello', () => {

        addSelected()

    })

    setInterval(updateDecorations,3000)

  /*  function test(){

        console.log("hallo")
    } */

    interface HighlightColors {
        light: string
        dark: string
    }

    let colors = {
           light: '#b3d9ff', dark: 'cyan' 
    } 

    

    let decorationType = window.createTextEditorDecorationType({
            borderWidth: '2px',
            borderStyle: 'solid',
            overviewRulerLane: OverviewRulerLane.Right,
            light: {
                // this color will be used in light color themes
                overviewRulerColor: colors.light,
                borderColor: colors.light,
                backgroundColor: colors.light
            },
            dark: {
                // this color will be used in dark color themes
                overviewRulerColor: colors.dark,
                borderColor: colors.dark
            }
        })
    
        function addSelected(){
                const editor = window.activeTextEditor
                let word = editor.document.getText(editor.selection)
               // console.log(word[7])
                let index0 = word.indexOf("(")
                let index1 = word.indexOf(",")
                let index2 = word.indexOf(")")
                
                let param1 = word.slice(index0+1,index1)
                let param2 = word.slice(index1+1,index2)
                //console.log(param2)
                word = word.replace(/strcpy\(\w+\,\w+\)/g, replace(param1,param2))          //replace
                let selection = editor.selection
                editor.edit(builder => {
                    builder.replace(selection, word)
                })
        }


        function replace(x,y){

            return "strncpy(" + x + "," + y + ",??)"

        }

        


        function updateDecorations(){
            const editor = window.activeTextEditor
            const text = editor.document.getText()
            let match
            let decs = []
            //const expression = word
            //const regEx = new RegExp(expression, 'g')
            while(match = regEx.exec(text)){
                const startPos = editor.document.positionAt(match.index);
                const endPos = editor.document.positionAt(match.index + match[0].length)
                const decoration = { range: new Range(startPos, endPos) }
                decs.push(decoration);
            }
            editor.setDecorations(decorationType,decs)

        




    

}


}

// this method is called when your extension is deactivated
export function deactivate() {
}