import {
    Navbar, 
    NavbarBrand, 
    NavbarContent, 
    NavbarItem, 
    NavbarMenuToggle,
    NavbarMenu,
    NavbarMenuItem
  } from "@nextui-org/navbar";

import { Link } from "@nextui-org/react";
import { Button } from "@nextui-org/react";
import { useState } from 'react'


export default function NavbarComponent() {
    const [isButtonActive, setIsButtonActive] = useState('camera');
    return (
        <Navbar isBlurred maxWidth="full" shouldHideOnScroll isBordered classNames={{
            item: [
              "flex",
              "relative",
              "h-full",
              "items-center",
              "data-[active=true]:after:content-['']",
              "data-[active=true]:after:absolute",
              "data-[active=true]:after:bottom-0",
              "data-[active=true]:after:left-0",
              "data-[active=true]:after:right-0",
              "data-[active=true]:after:h-[2px]",
              "data-[active=true]:after:rounded-[2px]",
              "data-[active=true]:after:bg-primary",
            ],
          }}>
          {/* Contenedor de la marca Hackathon */}
      <NavbarContent className="flex justify-start w-auto">
        <NavbarItem>
          <p className="font-bold text-white">SalesOnTime</p>
        </NavbarItem>
      </NavbarContent>

      {/* Contenedor de los enlaces centrados */}
      <NavbarContent className="absolute inset-0 flex justify-center" justify="center">
        <NavbarItem isActive={isButtonActive === 'camera'}>
          <Link 
            color={isButtonActive === 'camera' ? "primary" : "foreground"} 
            href="#" 
            onClick={() => setIsButtonActive('camera')}
          >
            Cámaras
          </Link>
        </NavbarItem>
        <NavbarItem isActive={isButtonActive === 'recommendation'}>
          <Link 
            color={isButtonActive === 'recommendation' ? "primary" : "foreground"} 
            href="#" 
            onClick={() => setIsButtonActive('recommendation')}
          >
            Recomendaciones
          </Link>
        </NavbarItem>
      </NavbarContent>
        </Navbar>
    
    );

}