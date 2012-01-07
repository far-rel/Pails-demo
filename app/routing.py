from Pails.core.routes import Route

r = Route()
account = r.resource('account', controller = 'user')
r.root('user', 'new')

#news = account.resources('news', only = 'show')
#comments = news.resources('comments',  without = ['destroy'])
#comments.member().post('some')
#comments.member().delete('some')
#news.collection().get('search')

#r = Route()
#admin = r.namespace('admin')
#admin.resources('news')

#r.match('admin', 'login', 'new')
#r.match('activate/:activation_token', 'user', 'activate', 'GET')
#r.match('account/news/:id', 'newsa', 'fgjk')
#r.root('login', 'new')

#routes = r.optimize()

#for (route, variables, controller, methods, name) in routes[0]:
    #for method in methods:
#        print "Address => %s Controller => %s Method => %s Action => %s Name => %s" % (route, controller, variables, methods, name)
        
#print routes[1].admin_news('dfghj', format = 'html')
