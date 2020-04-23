var systemDataCorrectModules = [];

class Copy_ColorMode {
	// 本来はテーブルから生成されるが、フレームワーク練習用なので直接JavaScriptで作っている
	
	getSupportedKeys() {
		// 790-090 : デフォルトのコピーカラーモード
		return [ "790-090" ];
	}

	getRequiredKeys() {
		// 780-169 : IOTカラーモード（カラー機か白黒機かの判定に使う）
		return [ "780-169" ];
	}

	correct(expected, required, corrected, failure) {
		
		// サポートしているデータがない場合は何もしない
		if (! expected["790-090"]) {
			return;
		}
		
		// 必要なデータが提供されない場合はエラーを応答する
		if (! required["780-169"]) {
			failure.push({"key" : "790-090", "value" : expected["790-090"], "reason" : "Required"});
			return;
		}
		
		if (required["780-169"] == 16) {
			// 白黒機の場合
			corrected["790-090"] = 2; // 白黒
			corrected["780-065"] = 0; // Copyのカラーモードのデフォルトに従う
			return;
		} else {
			// カラー機の場合
			corrected["790-090"] = 1; // 自動
			corrected["780-065"] = 0; // Copyのカラーモードのデフォルトに従う
			return;
		}
	}
}


systemDataCorrectModules.push(new Copy_ColorMode());

// // モジュールを集めるための配列 <= この宣言文はPython側で生成する
// var systemDataCorrectModules = [];

class SystemDataCorrector {
	
	constructor(modules) {
		this.modules = modules;
	}
	
	getSupportedKeys() {
		var ret = [];
		this.modules.forEach(function (module) {
			ret = ret.concat(module.getSupportedKeys());
		});
		return ret;
	}

	getRequiredKeys() {
		var ret = [];
		this.modules.forEach(function (module) {
			ret = ret.concat(module.getRequiredKeys());
		});
		return ret;
	}

	correct(expected, required, corrected, failure) {
		this.modules.forEach(function (module) {
            
			var ret_corrected = {};
			var ret_failure = [];
            
			module.correct(expected, required, ret_corrected, ret_failure);
			
			// 連想配列の結合
			corrected = Object.assign(corrected, ret_corrected);
			
			// 配列の結合（concatだと別のオブジェクトが作られてしまい、outパラメータにならないのでループでがんばる）
			ret_failure.forEach(function(value) {
				failure.push(value);
			});
		});
	}
}

