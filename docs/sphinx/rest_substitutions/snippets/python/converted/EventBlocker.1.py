    
        def DoSomething(self):
            # block all events directed to this window while
            # we do the 1000 FunctionWhichSendsEvents() calls
            blocker = wx.EventBlocker(self)

            for i in xrange(1000):
                FunctionWhichSendsEvents(i)
    
            # wx.EventBlocker destructor called, old event handler is restored
    
            # the event generated by this call will be processed:
            FunctionWhichSendsEvents(0)
        
