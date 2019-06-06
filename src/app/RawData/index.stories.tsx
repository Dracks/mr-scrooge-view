import React from 'react';
import { storiesOf } from '@storybook/react';

import Subject from '../Pages/RawDataPage';

import 'antd/dist/antd.css';
import ReduxDefaultData from 'stories/redux_tools';


storiesOf("RawData", module)
    .add("Complete table", ()=>(
        <ReduxDefaultData>
            <Subject />
        </ReduxDefaultData>
    ))
    .add("Testing", ()=><div>Test</div>)