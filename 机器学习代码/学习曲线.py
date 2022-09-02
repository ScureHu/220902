def plot_learning_curve(algo,x_train,x_test,y_train,y_test):
    train_score=[]
    test_score=[]
    for i in range(1,len(x_train)+1):
        
        algo.fit(x_train[:i],y_train[:i])
        
        y_train_predict = algo.predict(x_train[:i])
        train_score.append(mean_squared_error(y_train[:i],y_train_predict))
        
        y_test_predict = algo.predict(x_test)
        test_score.append(mean_squared_error(y_test,y_test_predict))
        
    plt.plot([i for i in range(1,len(x_train)+1)],
                        np.sqrt(train_score),label='train')
    plt.plot([i for i in range(1,len(x_train)+1)],
                        np.sqrt(test_score),label='test')
    plt.legend()
    plt.axis([0,len(x_train)+1,0,4])
    plt.show()