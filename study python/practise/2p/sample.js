var systemDataCorrectModules = [];

class Copy_ColorMode {
	// 本来はテーブルから生成されるが、フレームワーク練習用なので直接JavaScriptで作っている
	
	getSupportedKeys() {
		// xxx
		return [ "xxx" ];
	}

	getRequiredKeys() {
		// xxx
		return [ "xxx" ];
	}

	correct(expected, required, corrected, failure) {
		
		// xxx
		if (! expected["xxx"]) {
			return;
		}
		
		// 必要なデータが提供されない場合はエラーを応答する
		if (! required["xxx"]) {
			failure.push({"key" : "xxx "value" : expected["xxx"], "reason" : "Required"});
			return;
		}
		
		if (required["xxx"] == 16) {
			// xxxの場合
			corrected["xxx"] = 2; // xxx
			corrected["7xxx"] = 0; // xxx
			return;
		} else {
			// xxxの場合
			corrected["xxx"] = 1; // xxx
			corrected["xxx"] = 0; // xxx
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

