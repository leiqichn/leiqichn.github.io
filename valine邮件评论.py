export	SITE_NAME	Lei Qi的小宇宙	[必填] 博客名称
export	SITE_URL	https://leiqicn.gitee.io	[必填] 首页地址
export	SMTP_SERVICE	QQ	[必填] 邮件服务提供商，参照 Supported services
export	SMTP_USER	leeeqi@qq.com	[必填] SMTP 用户名
export	SMTP_PASS	hmmofkrphlocbaai	[必填] SMTP 授权码（非邮箱独立密码！），参照客户端设置
export	SENDER_NAME	Lei Qi	[必填] 发件人
export	SENDER_EMAIL	leeeiqi@qq.com	[必填] 发件邮箱
export	MAIL_SUBJECT	${PARENT_NICK}，您在${SITE_NAME}上的评论收到了回复	[必填]@通知邮件主题（标题）模板
export	MAIL_TEMPLATE	"<html>
<head></head> 
<body> 
  <div style=""border-radius: 10px 10px 10px 10px;font-size:13px; color: #555555;width: 666px;font-family:'Century Gothic','Trebuchet MS','Hiragino Sans GB',微软雅黑,'Microsoft Yahei',Tahoma,Helvetica,Arial,'SimSun',sans-serif;margin:50px auto;border:1px solid #eee;max-width:100%;background: #ffffff repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow: 0 1px 5px rgba(0, 0, 0, 0.15);""> 
  <div style=""width:100%;background:#49BDAD;color:#ffffff;border-radius: 10px 10px 0 0;background-image: -moz-linear-gradient(0deg, rgb(67, 198, 184), rgb(255, 209, 244));background-image: -webkit-linear-gradient(0deg, rgb(67, 198, 184), rgb(255, 209, 244));height: 66px;""> 
    <p style=""font-size:15px;word-break:break-all;padding: 23px 32px;margin:0;background-color: hsla(0,0%,100%,.4);border-radius: 10px 10px 0 0;color:#257db9"">您在<a style=""text-decoration:none;color:#257db9"" href=""${SITE_URL}"">「Kingpo's Note」</a>上的留言有新回复啦！</p>
  </div> 
  <div style=""margin:40px auto;width:90%""> 
    <p>亲爱的 <span style=""color:#7777ff"">${PARENT_NICK}</span> 同学，您曾在该页面/文章：</p> 
    <div style=""background: #fafafa repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);margin:20px 0px;padding:15px;border-radius:5px;font-size:14px;color:#555555;""> 
    ${POST_URL}
    </div> 
    <p>发布了以下评论：</p>
    <div style=""background: #fafafa repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);margin:20px 0px;padding:15px;border-radius:5px;font-size:14px;color:#555555;""> 
    <b>${PARENT_COMMENT} </b> 
    </div> 
    <p>刚刚，用户 <span style=""color:#7777ff"">${NICK}</span> 给您的回复如下：</p>
    <div style=""background: #fafafa repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);margin:20px 0px;padding:15px;border-radius:5px;font-size:14px;color:#555555;""> 
    <b>${COMMENT}</b> 
    </div> 
    <p>您可以点击 <a style=""text-decoration:none; color:#12addb"" href=""${POST_URL}#comments"">查看回复的完整內容</a>，欢迎再次光临<a style=""text-decoration:none; color:#9fefaf"" href=""${SITE_URL}""> ${SITE_NAME}</a>。</p>
    <style type=""text/css"">a:link{text-decoration:none}a:visited{text-decoration:none}a:hover{text-decoration:none}a:active{text-decoration:none}</style> 
  </div> 
  </div> 
  <center> 
  Powered by LeanCloud
</br>
  Copyright &copy; 2022 <a href=""https://kingpo.netlify.app"" style=""color:auto;"">六月长河</a>
  <br /> 
  <a href=""https://kingpo.netlify.app""><img style=""height:70px !important;"" src=""https://kingpo.netlify.app/images/avatar.png"" /></a> 
  </center> 
  <br /> 
  <br />  
</body>
</html>"	[必填]@通知邮件内容模板
export	MAIL_SUBJECT_ADMIN	${SITE_NAME}上有新评论了	[必填] 博主邮件通知主题模板
export	MAIL_TEMPLATE_ADMIN	"<html>
<head></head>
<body>
  <div style=""border-top:2px solid #12ADDB;box-shadow:0 1px 3px #AAAAAA;line-height:180%;padding:0 15px 12px;margin:50px auto;font-size:12px;""> 
  <h2 style=""border-bottom:1px solid #DDD;font-size:14px;font-weight:normal;padding:13px 0 10px 0px;"">您在<a style=""text-decoration:none;color: #12ADDB;"" href=""${SITE_URL}"" target=""_blank"">${SITE_NAME}</a>上的文章有了新的评论</h2> 
  <p><strong>${NICK}</strong>回复说：</p>
  <div style=""background-color: #f5f5f5;padding: 10px 15px;margin:18px 0;word-wrap:break-word;"">
    ${COMMENT}
  </div>
  <p> 您可以点击<a style=""text-decoration:none; color:#12addb"" href=""${POST_URL}"" target=""_blank"">查看回复的完整內容</a><br /></p> 
  <p><strong>评论页面为</strong></p>
  <p><strong>${POST_URL}</strong></p>
  <br />
  </div>
</body>
</html>"	[必填] 博主邮件通知内容模板
export	SMTP_HOST	smtp.qq.com	[必填] SMTP_SERVICE 留空时，自定义 SMTP 服务器地址
export	SMTP_PORT	465	[必填] SMTP_SERVICE 留空时，自定义 SMTP 端口
export	SMTP_SECURE	TRUE	[选填] SMTP_SERVICE 留空时填写
export	BLOGGER_EMAIL		[选填] 博主通知收件地址，默认使用 SENDER_EMAIL
export	ADMIN_URL	https://leiqicn.gitee.io	评论管理后台地址
export	COMMENT		新评论内容
export	NICK		新评论者昵称
export	PARENT_COMMENT		父级评论内容
export	PARENT_NICK		收件人昵称（被@者，父级评论人）
export	POST_URL		评论文章地址（完整路径）
