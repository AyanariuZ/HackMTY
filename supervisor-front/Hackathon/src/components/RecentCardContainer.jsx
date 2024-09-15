import React from 'react'

export const RecentCardContainer = ({children}) => {
  return (
    <div className='grid grid-cols-4 dark bg-black'> 
    {children}
    </div>
  )
}
