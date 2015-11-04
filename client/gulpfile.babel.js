import gulp       from 'gulp';
import babelify   from 'babelify';
import browserify from 'browserify';
import source     from 'vinyl-source-stream';
import buffer     from 'vinyl-buffer';
import sourcemaps from 'gulp-sourcemaps';

let paths = {
    test: "./static/test/*.js",
    src: "./static/js/",
    dist_src: "./static/build/js/"
};


gulp.task('browserify', () => {
    browserify({entries: [paths.src + "app.js"]})
        .transform(babelify)
        .bundle()
        .pipe(source("bundle.js"))
        .pipe(buffer())
        .pipe(sourcemaps.init({loadMaps: true}))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(paths.dist_src));
});

gulp.task('watch', () => {
    gulp.watch(paths.src + '**/*', ['browserify'])
});

gulp.task('default', ['watch']);
