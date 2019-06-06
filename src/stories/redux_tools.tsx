import React from 'react';
import { Provider } from 'react-redux';
import { createStore } from  'redux';

import reducers from '../reducers';
import { ITag, IFileKind, IRawData } from 'types/data';

const fakeNetworkResponse = (data)=>({isLoading:false, data})

const tags: ITag[] = [
    {id: 1, name: "peperoni"},
    {id: 1, name: "dalek"},
]

const importFileKinds : IFileKind[] = [
    {key: "Caixa", regexp:/alskdjf/}
]

const allData: IRawData[] = Array.from(Array(100).keys()).map((id)=>({
    id,
    kind: importFileKinds[0].key,
    tags: tags.filter(()=>Math.random()<0.3).map(({id})=>id),
    movement_name: "Movement name "+id,
    value: Math.random()*1000,
    date: new Date()
}))

const hashTags = tags.reduce((ac, e)=>({[e.id]:e, ...ac}), {})

const store = createStore(reducers({}), {
    tags: fakeNetworkResponse(tags),
    importFileKinds: fakeNetworkResponse(importFileKinds),
    allData: fakeNetworkResponse(allData),
    hashTags
});

const ReduxDefaultData = ({children})=>(
    <Provider store={store}>
        {children}
    </Provider>
)

export default ReduxDefaultData
