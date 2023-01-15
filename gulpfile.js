var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('autoprefixer');
var concat = require('gulp-concat');
var postcss = require('gulp-postcss');
var sourcemaps = require('gulp-sourcemaps');
var browserSync = require('browser-sync').create();
var reload = browserSync.reload;

// Run the Django development server
gulp.task('django', function() {
    const spawn = require('child_process').spawn;
    return spawn('python', ['project/manage.py', 'runserver'])
        .stderr.on('data', (data) => {
        console.log(`${data}`);
    });
});

// Compile main.sass into style.css
gulp.task('styles', function() {
    gulp.src('./project/home/static/sass/main.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('style.css'))
        .pipe(sourcemaps.init())
        .pipe(postcss([autoprefixer() ]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./project/home/static/css/'));
});

// Initiate browsersync and point it at localhost:8000
gulp.task('browsersync', function() {
    browserSync.init({
        notify: true,
        proxy: "localhost:8000",
    });
});

// Tell gulp to executed 'styles' when sass files change, and execute
// a browser reload when any file changes.
gulp.task('watch', function() {
    gulp.watch('./project/home/static/sass/**/*.sass', ['styles']);
    gulp.watch(['./**/*.{sass,css,html,py,js}'], reload);
});

// 'gulp' calls django, browsersync, and watch tasks
gulp.task('default', ['django', 'browsersync', 'watch']);