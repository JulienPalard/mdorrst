# lektor-gulp #

This plugin for [Lektor static CMS](https://www.getlektor.com) adds [gulp](http://gulpjs.com) support to projects. When enabled with the `-f gulp` flag it runs `npm install` and then the gulp default or watch tasks as they are defined into the standard gulpfile.js file.

## lektor build ##

The command `lektor build -f gulp` runs the **default** gulp task, for example defined as:

```javascipt
gulp.task('build', ['clean', 'copy', 'js', 'css', 'imagemin'], () => { });

gulp.task('default', ['build'], () => { });
``` 

In this example the default task points to a build task, which is usually composed by several other tasks, etc.

## lektor server ##

The command `lektor server -f gulp` runs the Lektor server on http://localhost:5000, starting a gulp **watch** task in background. For example, you can define something such as:

```javascript
gulp.task('watch', () => {
    gulp.watch('lib/js/**/*.js', ['js']);
    gulp.watch('lib/css/**/*.css', ['css']);
});
```

In this case, each time one touchs Javascript or CSS files in the lib/ folder then assets can be minified, concatenated and copied into the standard `assets/static/` lektor folder. What happens is under complete control of your own gulpfile.js.

## Credits ##

This plugin is mostly a clone of the official [Webpack plugin](https://github.com/lektor/lektor-webpack-support) with very little differences.
