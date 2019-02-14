/*
 * Copyright 2017 anonymous
 *
 * This software is the result of a joint project between anonymous and anonymous
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 *     Unless required by applicable law or agreed to in writing, software
 *     distributed under the License is distributed on an "AS IS" BASIS,
 *     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *     See the License for the specific language governing permissions and
 *     limitations under the License.
 */

/**
 * \file
 *
 * \author anonymous
 * \date February 19, 2015
 *
 * \author anonymous + anonymous
 * \date Feb 2017
 *
 * This holds stuff useful across the whole application.
 */

#ifndef MOONSHINE_H
#define MOONSHINE_H

#include <valarray>
#include <vector>

#include <boost/log/sources/global_logger_storage.hpp>
#include <boost/log/trivial.hpp>

using INDEX = int;    // a column index
using BIN_ELEM = int; // a single binary (0 or 1) element of the matrix
using ROW = std::vector<BIN_ELEM>;    // a 0-1 vector of a row from the matrix
using COLUMN = std::vector<BIN_ELEM>; // a 0-1 vector of a col from the matrix
using COL_DATA = std::vector<INDEX>;  // the column data stored for each row
using INDEX_LIST = std::vector<INDEX>;
using COLUMN_SUM = std::vector<int>;
using ROW_SUM = std::vector<int>;
using MEASURE = std::vector<double>;

// logging joy
#define BOOST_LOG_DYN_LINK 1

// we define our own severity levels
enum severity_level { debug, info, warning, error, critical };
BOOST_LOG_GLOBAL_LOGGER(my_logger, boost::log::sources::severity_logger<>)

#endif /* MOONSHINE_H */
