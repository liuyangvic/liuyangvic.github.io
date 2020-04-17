### Learn JavaScript付録：JavaScript実行環境

LinuxのCからJavaScriptを実行する
node.jsによるコマンドラインツール
https://qiita.com/akameco/items/585f2c53629f1e66f4f1

Node.jsでコマンドラインツールを作成
https://medium.com/@kaoru.mori/node-js%E3%81%A7%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%84%E3%83%BC%E3%83%AB%E3%82%92%E4%BD%9C%E6%88%90-290645fa7654


Node.js入門１　コマンドラインからの色々な実行方法
https://symfoware.blog.fc2.com/blog-entry-2105.html

$ node -e "console.log('hello world\!')"
hello world!

$ node sample.js
hello world!


Emscripten(C/C++) と JavaScript 間の関数呼び出し方法 まとめ
https://www.sumiretool.net/docs/tech/emscriptencc-%E3%81%A8-javascript-%E9%96%93%E3%81%AE%E9%96%A2%E6%95%B0%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%97%E6%96%B9%E6%B3%95-%E3%81%BE%E3%81%A8%E3%82%81/


V8の基本的なAPIを学ぶ
https://qiita.com/komukomo/items/316afadd04f95808f338

V8 API
https://v8docs.nodesource.com/node-0.8/d0/d35/classv8_1_1_script.html
v8::Script::Compile にスクリプトを指定する


JavaからJavaScriptを実行

https://www.javalife.jp/2018/04/01/post-508/
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class JavaScriptTest {
	public static void main(String[] args) {
		new JavaScriptTest().execute("var a = 1 + 2; print('1 + 2 = '+a);");
	}
	public void execute(String script) {
		ScriptEngineManager sem = new ScriptEngineManager();
		ScriptEngine se = sem.getEngineByName("JavaScript");
		try {
			se.eval(script);
		} catch (ScriptException e) {
			e.printStackTrace();
		}
	}
