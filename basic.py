from zk import ZK , const
conn= None
zk=ZK('10.165.13.31', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)

try:
    # connect to device
    conn = zk.connect()
    # disable device, this method ensures no activity on the device while the process is run
    conn.disable_device()
    # another commands will be here!
    # Example: Get All Users
    users = conn.get_users()
    for user in users:
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'
        print ('+ UID #{}'.format(user.uid))
        print ('  Name       : {}'.format(user.name))
        print ('  Privilege  : {}'.format(privilege))
        print ('  Password   : {}'.format(user.password))
        print ('  Group ID   : {}'.format(user.group_id))
        print ('  User  ID   : {}'.format(user.user_id))
        print ('  User  Card   : {}'.format(user.card))
        

    # Test Voice: Say Thank You
    #conn.test_voice()
    # re-enable device after all commands already executed

    

    atts = conn.get_attendance()
    for att in atts:
        print ('+ UID #{}'.format(att.uid))
        print ('  User id      : {}'.format(att.user_id))
        print ('  Timestamp  : {}'.format(att.timestamp))
        print ('  Status   : {}'.format(att.status))
        print ('  Punch   : {}'.format(att.punch))


    conn.enable_device()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()