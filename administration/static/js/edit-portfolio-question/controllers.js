(function(angular){

    var app = angular.module('edit-portfolio-question');

    app.controller('EditPortfolioQuestionController', ['$scope', 'Course', 'CourseProfessor', 'VideoData', 'youtubePlayerApi', 'MarkdownDirective', 'waitingScreen','PortfolioQuestion',
        function($scope, Course, CourseProfessor, VideoData, youtubePlayerApi, MarkdownDirective, waitingScreen, PortfolioQuestion){
            $scope.errors = {};
            var httpErrors = {
                '400': 'Os campos não foram preenchidos corretamente.',
                '403': 'Você não tem permissão para ver conteúdo nesta página.',
                '404': 'Este curso não existe!'
            };

            // load youtube
            $scope.playerReady = false;
            youtubePlayerApi.loadPlayer().then(function(p){
                $scope.playerReady = true;
            });

            // show the waiting screen
            waitingScreen.show();

            $scope.play = function(youtube_id) {
                youtubePlayerApi.loadPlayer().then(function(player){
                    if(player.getVideoData().video_id === youtube_id) return;
                    player.cueVideoById(youtube_id);
                });
            };

            $scope.course = new Course();
            $scope.portfolioquestion = new PortfolioQuestion();

            $scope.courseProfessors = [];


            /*  Methods */

             /*  TITLE OF THE PAGE */
            $scope.setPortfolioQuestion = function(l) {
                $scope.portfolioquestion = l;
                document.title = 'Aula: {0}'.format(l.title);
            };


            $scope.savePortfolioQuestion = function() {
                    $scope.portfolioquestion.saveOrUpdate()
                    .then(function(){
                        $scope.alert.success('Alterações salvas com sucesso.');
                    })['catch'](function(resp){
                        $scope.alert.error(httpErrors[resp.status.toString()]);
                    });
            };


            $scope.publishPortfolioQuestion = function() {
                $scope.portfolioquestion.status = 'published';
                $scope.savePortfolioQuestion();
            };

            $scope.deletePortfolioQuestion = function() {
                var msg = 'Apagar a aula "'+ $scope.portfolioquestion.title + '" e todo seu conteúdo?';

                if(!confirm(msg)) return;

                function backToCourse () {
                    document.location.href = '/admin/courses/{0}'
                                             .format($scope.course.id);
                }
                if(true) {

                    if($scope.portfolioquestion.id){
                        msg = 'A Portfolio Question do aula "{0}" e todo seu conteúdo foram apagados do sistema.'
                              .format($scope.portfolioquestion.title);
                        $scope.portfolioquestion.$delete().then(function(){
                            $scope.alert.success(msg);
                            backToCourse();
                        });
                    } else {
                        backToCourse();
                    }
                } else {
                    $scope.portfolioquestion = new PortfolioQuestion();
                }
            };


             $scope.setPortfolioQuestionVideo = function() {
                var youtube_id = $scope.portfolioquestion.intended_youtube_id;
                if(!$scope.portfolioquestion.video) {
                    $scope.portfolioquestion.video = {};
                }
                 $scope.portfolioquestion.video.youtube_id = youtube_id;
                VideoData.load(youtube_id).then(function(data){
                 $scope.portfolioquestion.video.name = data.entry.title.$t;


                });

                $scope.play(youtube_id);
            };
   /*  End Methods */


            // vv como faz isso de uma formula angular ?
            var match = document.location.href.match(/courses\/(\d+)\/portfolios\/(new|\d+)/);
            if( match ) {
                $scope.isNewPortfolioQuestion = ('new' === match[2]);

                $scope.course.$get({id: match[1]})
                    .then(function(course){
                        $scope.courseProfessors = CourseProfessor.query({ course: course.id });
                        $scope.portfolioquestion.course = course.id;
                        $scope.course_url = 'admin/courses/' + course.id;
                        $scope.course_material_url = 'admin/course/' + course.id  + '/material/';
                        $scope.forum_url = 'admin/course/' + course.id +  '/forum/';
                        $scope.messages_url = 'admin/course/' + course.id   + '/messages/';
                        $scope.reports_url = 'admin/course/' + course.id   + '/stats/';


                        return $scope.courseProfessors.$promise;
                    });

                PortfolioQuestion.query({course__id: match[1]}).$promise
                    .then(function(portfolio_questions){
                        $scope.portfolio_questions = portfolio_questions;
                        portfolio_questions.forEach(function(portfolioquestion){
                            if(portfolioquestion.id === parseInt(match[2], 10)) {
                                if (portfolioquestion.video) {
                            youtubePlayerApi.videoId = portfolioquestion.video.youtube_id;
                        }
                                $scope.setPortfolioQuestion(portfolioquestion);
                            }
                        });
                        if($scope.isNewPortfolioQuestion) {


                            $scope.portfolio_questions.push($scope.portfolioquestion);
                        }
                        waitingScreen.hide();
                    })['catch'](function(resp){
                        $scope.alert.error(httpErrors[resp.status.toString()]);
                        waitingScreen.hide();
                    });
            }
            // ^^ como faz isso de uma formula angular ?
        }
    ]);


})(window.angular);
