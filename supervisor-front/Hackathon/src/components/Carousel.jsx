import RecoCard from './RecoCard'
import React from 'react'
import {ScrollShadow} from "@nextui-org/react";

export default function Component({children}) {
  // Creamos un array de 10 elementos para simular múltiples tarjetas

  return (
<div className="w-full max-w-[1200px] mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4 text-white">Ofertas recientes</h2>
      <div className="relative">
      
        <div className="overflow-x-auto pb-4 hide-scrollbar">
        <ScrollShadow 
        orientation="horizontal" 
        className="max-w-full" 
        offset={40}
        hideScrollBar
      >
          <div className="flex space-x-4">
          {React.Children.map(children, (child, index) => (
              <div className="flex-none" key={index}>
                {child}
              </div>
            ))}
          </div>
          </ScrollShadow>
        </div>
        
      </div>
      

    </div>

  
  
  )
}

// Estilos adicionales para ocultar la barra de desplazamiento en algunos navegadores
