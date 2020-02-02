//
//  LoginViewController.swift
//  helloworld2
//
//  Created by Joya Das on 2/2/20.
//  Copyright © 2020 Joya Das. All rights reserved.
//

import Foundation
import UIKit

class LoginViewController:UIViewController{
    @IBOutlet weak var userNameTextField: UIStackView!
    @IBOutlet weak var passwordTextField: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    @IBAction func loginTapped(_ sender: Any) {
    }
    
    private func navigateToMainInterface(){
        let mainStoryboard = UIStoryboard(name: "Main", bundle: Bundle.main)
        
        guard let mainNavigationVC = mainStoryboard.instantiateViewController(withIdentifier: "MainNavigationController") as? MainNavigationController else{
            return
        }
        
        present(mainNavigationVC, animated:true, completion:nil)
    }
}
