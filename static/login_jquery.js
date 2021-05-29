$(document).ready(function() {
  $('#login_area-jq').hide();
  $('#register_area-jq').hide();

  $('#register_btn-jq').on('click',function() {
    $('#intro_area-jq').hide();
    $('#login_area-jq').hide();
    $('#register_area-jq').show();
  });
  $('#register_btn1-jq').on('click',function() {
    $('#intro_area-jq').hide();
    $('#login_area-jq').hide();
    $('#register_area-jq').show();
  });
  $('#login_btn-jq').on('click',function() {
    $('#intro_area-jq').hide();
    $('#register_area-jq').hide();
    $('#login_area-jq').show();
  });
  $('#community-home').on('click',function() {
    $('#login_area-jq').hide();
    $('#register_area-jq').hide();
    $('#intro_area-jq').show();
  });
});