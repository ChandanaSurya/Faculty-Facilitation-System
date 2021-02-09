def viewfaculty():
    username = session.get('username',None)
    l = []
    cse  = []
    it  = []
    ece = []
    eee = []
    mba = []
    mca = []
    ce = []
    me = []
    fed = []
    ae = []
    others = []
    script = False
    x = mysql.connection.cursor()
    x.execute('select id from user1')
    y = x.fetchall()
    count = 0
    for i in y:
        l.append(i)
        count = count + 1
    if count > 0:
        script = True
        l.sort()
        for i in l:
            j=''
            j =''.join(i)
            if j.startswith('cse',0,3):
                cse.append(j)
            elif j.startswith('ece',0,3):
                ece.append(j)
            elif j.startswith('it',0,2):
                it.append(j)
            elif j.startswith('eee',0,3):
                eee.append(j)
            elif j.startswith('fed',0,3):
                fed.append(j)
            elif j.startswith('mba',0,3):
                mba.append(j)
            elif j.startswith('mca',0,3):
                mca.append(j)
            elif j.startswith('ce',0,2):
                ce.append(j)
            elif j.startswith('me',0,2):
                me.append(j)
            elif j.startswith('ae',0,2):
                ae.append(j)
            else:
                others.append(j)
    else:
        return render_template('viewfaculty.html',username=username,script=script)
    if request.method == 'POST':
        id = request.form['id']
        if id == '':
            flash('Enter a valid ID......')
            return render_template('viewfaculty.html',username=username,script=script,cse=cse,it=it,ece=ece,eee=eee,fed=fed,mba=mba,mca=mca,ce=ce,me=me,ae=ae,others=others)
        x = mysql.connection.cursor()
        x.execute('select * from user1 where id=%s',(id,))
        y = x.fetchall()
        x.close()
        gc.collect()
        count = 0
        for i in y:
            count = count + 1
        if count > 0:
            x = mysql.connection.cursor()
            x.execute('delete from user1 where id = %s',(id,))
            x.connection.commit()
            x.close()
            flash('Deleted successfullt..')
            gc.collect()
            return render_template('viewfaculty.html',username=username,script=script,cse=cse,it=it,ece=ece,eee=eee,fed=fed,mba=mba,mca=mca,ce=ce,me=me,ae=ae,others=others)
        else:
            flash('Faculty account for entered id is not available...')
            return render_template('viewfaculty.html',username=username,script=script,cse=cse,it=it,ece=ece,eee=eee,fed=fed,mba=mba,mca=mca,ce=ce,me=me,ae=ae,others=others)
    return render_template('viewfaculty.html',username=username,script=script,cse=cse,it=it,ece=ece,eee=eee,fed=fed,mba=mba,mca=mca,ce=ce,me=me,ae=ae,others=others)

